#!/usr/bin/env python3
"""
Render FUGUEJUKEBOX variations to audio with effects.

Converts note data + effect specifications into WAV/MP3 files with:
- NES-style synthesizer tones (square, triangle, pulse waves)
- Harmonic harmonies
- Scale runs and arpeggios
- Effect processing (reverb, vibrato, delay)

Uses scipy.io.wavfile for synthesis + pydub for effects + effects chains.
"""

import json
import os
import sys
import subprocess
from pathlib import Path
from typing import List, Tuple, Optional
import logging
import numpy as np
from scipy.io import wavfile
from scipy import signal

# Try to import audio libs; provide graceful fallback
try:
    from pydub import AudioSegment
    from pydub.generators import Sine, Square, Triangle
    from pydub.exceptions import CouldntDecodeError
    HAS_PYDUB = True
except ImportError:
    HAS_PYDUB = False
    logging.warning("pydub not installed — will skip MP3 export (audio will be WAV only)")

try:
    import librosa
    HAS_LIBROSA = True
except ImportError:
    HAS_LIBROSA = False

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
log = logging.getLogger(__name__)

# Paths
PROJECT_ROOT = Path(__file__).parent
OUTPUT_DIR = PROJECT_ROOT / "emblems"
METADATA_DIR = PROJECT_ROOT / "metadata"

# Synthesis parameters
SAMPLE_RATE = 44100
NES_SYNTH_TYPE = 'square'  # 'square', 'triangle', 'sine'
A4_FREQ = 440.0


def midi_to_freq(midi: int) -> float:
    """Convert MIDI note number to frequency in Hz."""
    return A4_FREQ * (2.0 ** ((midi - 69) / 12.0))


def generate_tone(freq: float, duration: float, sample_rate: int = SAMPLE_RATE,
                  synth_type: str = 'sine', attack: float = 0.01, release: float = 0.1) -> np.ndarray:
    """
    Generate a single tone with ADSR envelope.

    Args:
        freq: Frequency in Hz
        duration: Duration in seconds
        sample_rate: Samples per second
        synth_type: 'sine', 'square', 'triangle'
        attack: Attack time in seconds
        release: Release time in seconds
    """
    samples = int(duration * sample_rate)
    t = np.arange(samples, dtype=np.float32) / sample_rate

    # Generate waveform
    if synth_type == 'square':
        # Crude square wave via sign of sine
        wave = np.sign(np.sin(2 * np.pi * freq * t))
    elif synth_type == 'triangle':
        # Triangle wave via arcsin
        wave = 2 * np.arcsin(np.sin(2 * np.pi * freq * t)) / np.pi
    else:  # 'sine'
        wave = np.sin(2 * np.pi * freq * t)

    # ADSR envelope
    attack_samples = int(attack * sample_rate)
    release_samples = int(release * sample_rate)
    sustain_samples = samples - attack_samples - release_samples

    envelope = np.ones(samples, dtype=np.float32)

    # Attack
    if attack_samples > 0:
        envelope[:attack_samples] = np.linspace(0, 1, attack_samples)

    # Release
    if release_samples > 0:
        envelope[-release_samples:] = np.linspace(1, 0.01, release_samples)

    return wave * envelope * 0.6  # 0.6 to leave headroom


def render_notes_to_audio(notes: List[List[float]], bpm: float,
                          synth_type: str = 'square') -> np.ndarray:
    """
    Render a list of notes to audio samples.

    Notes format: [[start_beat, duration_beat, midi_pitch], ...]
    """
    beat_duration = 60.0 / bpm  # seconds per beat

    # Calculate total duration
    max_time = max((n[0] + n[1] for n in notes), default=1.0)
    total_samples = int(max_time * beat_duration * SAMPLE_RATE) + SAMPLE_RATE

    audio = np.zeros(total_samples, dtype=np.float32)

    for start_beat, dur_beat, midi in notes:
        start_sec = start_beat * beat_duration
        dur_sec = dur_beat * beat_duration

        # Skip rests (MIDI 0)
        if midi == 0:
            continue

        freq = midi_to_freq(int(midi))
        tone = generate_tone(freq, dur_sec, synth_type=synth_type)

        # Mix into audio
        start_sample = int(start_sec * SAMPLE_RATE)
        end_sample = start_sample + len(tone)

        if end_sample <= total_samples:
            audio[start_sample:end_sample] += tone
        else:
            # Truncate if exceeds bounds
            audio[start_sample:] += tone[:total_samples - start_sample]

    # Normalize to prevent clipping
    max_val = np.max(np.abs(audio))
    if max_val > 0:
        audio = audio / (max_val * 1.05)  # Small headroom

    return audio


def apply_reverb(audio: np.ndarray, wet: float = 0.3, decay: float = 1.5,
                 sample_rate: int = SAMPLE_RATE) -> np.ndarray:
    """
    Apply simple reverb via convolution with an exponential decay impulse.

    Args:
        audio: Audio samples
        wet: Wet signal level (0.0 - 1.0)
        decay: Decay time in seconds
        sample_rate: Sample rate
    """
    if wet <= 0:
        return audio

    # Create exponential decay impulse response
    ir_samples = int(decay * sample_rate)
    t = np.arange(ir_samples, dtype=np.float32) / sample_rate
    ir = np.exp(-3 * t / decay) * np.cos(2 * np.pi * 50 * t)  # 50 Hz modulation
    ir = ir / np.max(np.abs(ir))

    # Convolve
    reverb = signal.fftconvolve(audio, ir, mode='same')
    reverb = reverb / np.max(np.abs(reverb)) if np.max(np.abs(reverb)) > 0 else reverb

    # Mix wet and dry
    return (1.0 - wet) * audio + wet * reverb


def apply_vibrato(audio: np.ndarray, depth: float = 0.1, rate: float = 5.0,
                  sample_rate: int = SAMPLE_RATE) -> np.ndarray:
    """
    Apply vibrato (frequency modulation) to audio.

    Args:
        audio: Audio samples
        depth: Vibrato depth (0.0 - 0.2 recommended)
        rate: Vibrato rate in Hz
        sample_rate: Sample rate
    """
    if depth <= 0:
        return audio

    samples = len(audio)
    t = np.arange(samples, dtype=np.float32) / sample_rate

    # LFO (low-frequency oscillator)
    lfo = np.sin(2 * np.pi * rate * t)

    # Apply vibrato as pitch modulation (simple version: amplitude mod + pitch mod)
    vibrato = audio * (1.0 + depth * lfo * 0.5)
    vibrato = vibrato / np.max(np.abs(vibrato)) if np.max(np.abs(vibrato)) > 0 else vibrato

    return vibrato


def apply_tremolo(audio: np.ndarray, depth: float = 0.1, rate: float = 4.0,
                  sample_rate: int = SAMPLE_RATE) -> np.ndarray:
    """
    Apply tremolo (amplitude modulation) to audio.
    """
    if depth <= 0:
        return audio

    samples = len(audio)
    t = np.arange(samples, dtype=np.float32) / sample_rate

    # Amplitude modulation
    lfo = np.sin(2 * np.pi * rate * t)
    tremolo = audio * (1.0 - depth + depth * lfo)

    return tremolo


def apply_delay(audio: np.ndarray, delay_times: List[float], feedback: float = 0.4,
                wet: float = 0.3, sample_rate: int = SAMPLE_RATE) -> np.ndarray:
    """
    Apply multi-tap delay with feedback.

    Args:
        audio: Audio samples
        delay_times: List of delay times in seconds
        feedback: Feedback coefficient (0.0 - 0.9)
        wet: Wet signal level
        sample_rate: Sample rate
    """
    if wet <= 0 or not delay_times:
        return audio

    output = audio.copy()

    for delay_sec in delay_times:
        delay_samples = int(delay_sec * sample_rate)
        if delay_samples < 1 or delay_samples >= len(audio):
            continue

        # Create delayed signal
        delayed = np.zeros_like(audio)
        delayed[delay_samples:] = audio[:-delay_samples]

        # Mix with feedback
        for _ in range(int(feedback / 0.1)):  # Simple feedback iterations
            if np.max(np.abs(delayed)) < 1e-6:
                break
            delayed[delay_samples:] += delayed[:-delay_samples] * feedback

        output = output + wet * delayed

    # Normalize
    max_val = np.max(np.abs(output))
    if max_val > 1.0:
        output = output / (max_val * 1.05)

    return output


def apply_effects(audio: np.ndarray, effects_config: dict,
                  sample_rate: int = SAMPLE_RATE) -> np.ndarray:
    """
    Apply all effects from configuration to audio.
    """
    output = audio.copy()

    # Reverb
    reverb_wet = effects_config.get('reverb_wet', 0)
    if reverb_wet > 0:
        reverb_decay = effects_config.get('reverb_decay', 1.5)
        output = apply_reverb(output, wet=reverb_wet, decay=reverb_decay, sample_rate=sample_rate)
        log.debug(f"  Applied reverb (wet={reverb_wet}, decay={reverb_decay}s)")

    # Vibrato
    vibrato_depth = effects_config.get('vibrato_depth', 0)
    if vibrato_depth > 0:
        vibrato_rate = effects_config.get('vibrato_rate', 5.0)
        output = apply_vibrato(output, depth=vibrato_depth, rate=vibrato_rate, sample_rate=sample_rate)
        log.debug(f"  Applied vibrato (depth={vibrato_depth}, rate={vibrato_rate}Hz)")

    # Tremolo
    tremolo_depth = effects_config.get('tremolo_depth', 0)
    if tremolo_depth > 0:
        tremolo_rate = effects_config.get('tremolo_rate', 4.0)
        output = apply_tremolo(output, depth=tremolo_depth, rate=tremolo_rate, sample_rate=sample_rate)
        log.debug(f"  Applied tremolo (depth={tremolo_depth}, rate={tremolo_rate}Hz)")

    # Delay
    delay_wet = effects_config.get('delay_wet', 0)
    if delay_wet > 0 and 'delay_times' in effects_config:
        delay_times = effects_config['delay_times']
        delay_feedback = effects_config.get('delay_feedback', 0.4)
        output = apply_delay(output, delay_times, feedback=delay_feedback, wet=delay_wet, sample_rate=sample_rate)
        log.debug(f"  Applied delay (times={delay_times}, feedback={delay_feedback})")

    return output


def save_wav(audio: np.ndarray, filepath: Path, sample_rate: int = SAMPLE_RATE) -> bool:
    """Save audio to WAV file."""
    try:
        # Convert to 16-bit PCM
        audio_int16 = np.int16(audio * 32767)
        wavfile.write(str(filepath), sample_rate, audio_int16)
        log.debug(f"  Saved WAV: {filepath}")
        return True
    except Exception as e:
        log.error(f"  Failed to save WAV: {e}")
        return False


def convert_to_mp3(wav_path: Path, mp3_path: Path) -> bool:
    """Convert WAV to MP3 using ffmpeg or pydub."""
    if not wav_path.exists():
        return False

    try:
        # Try ffmpeg first (faster)
        result = subprocess.run(
            ['ffmpeg', '-i', str(wav_path), '-q:a', '5', str(mp3_path), '-y'],
            capture_output=True, timeout=30
        )
        if result.returncode == 0:
            log.debug(f"  Converted to MP3 via ffmpeg: {mp3_path}")
            return True
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass

    # Fallback to pydub
    if HAS_PYDUB:
        try:
            sound = AudioSegment.from_wav(str(wav_path))
            sound.export(str(mp3_path), format='mp3', bitrate='192k')
            log.debug(f"  Converted to MP3 via pydub: {mp3_path}")
            return True
        except Exception as e:
            log.error(f"  pydub conversion failed: {e}")
            return False

    log.warning(f"  Could not convert to MP3 (ffmpeg/pydub not available): {wav_path}")
    return False


def render_emblem_variations(emblem_num: int, variations_metadata: dict) -> int:
    """
    Render all 10 variations for a single emblem to audio files.
    Returns count of successfully rendered variations.
    """
    emblem_dir = OUTPUT_DIR / f"emblem_{emblem_num:02d}"
    emblem_dir.mkdir(parents=True, exist_ok=True)

    rendered_count = 0

    for var_meta in variations_metadata.get('variations', []):
        var_num = var_meta['variation_num']
        var_name = var_meta['name']
        notes = var_meta['notes']
        bpm = var_meta['bpm']
        effects_config = var_meta.get('effects', {})

        log.info(f"  Emblem {emblem_num:2d} / Variation {var_num:2d}: {var_name}")

        # Render notes to audio
        audio = render_notes_to_audio(notes, bpm, synth_type=NES_SYNTH_TYPE)

        # Apply effects
        if effects_config:
            audio = apply_effects(audio, effects_config)

        # Save as WAV
        wav_filename = f"emblem_{emblem_num:02d}_variation_{var_num:02d}.wav"
        wav_path = emblem_dir / wav_filename
        if not save_wav(audio, wav_path):
            continue

        # Convert to MP3
        mp3_filename = f"emblem_{emblem_num:02d}_variation_{var_num:02d}.mp3"
        mp3_path = emblem_dir / mp3_filename
        if convert_to_mp3(wav_path, mp3_path):
            rendered_count += 1
            log.info(f"    ✓ {mp3_filename}")
        else:
            log.warning(f"    ⚠ MP3 export failed, WAV available: {wav_filename}")
            rendered_count += 1  # Count WAV as successful too

    return rendered_count


def main():
    log.info("=== Rendering FUGUEJUKEBOX Audio ===")

    # Load metadata
    global_meta_file = METADATA_DIR / "all_variations.json"
    if not global_meta_file.exists():
        log.error(f"Metadata not found: {global_meta_file}")
        log.info("Run generate_variations.py first")
        sys.exit(1)

    with open(global_meta_file, 'r') as f:
        all_metadata = json.load(f)

    log.info(f"Rendering {len(all_metadata)} emblems × 10 variations = {len(all_metadata) * 10} audio files")

    total_rendered = 0

    for emblem_num in sorted(int(k) for k in all_metadata.keys()):
        emblem_meta = all_metadata[str(emblem_num)]
        rendered = render_emblem_variations(emblem_num, emblem_meta)
        total_rendered += rendered

    log.info(f"\n✓ Rendered {total_rendered} / {len(all_metadata) * 10} audio files")
    log.info(f"✓ Output directory: {OUTPUT_DIR}")
    log.info("\nNext: Sample MP3s from each emblem folder!")


if __name__ == '__main__':
    main()
