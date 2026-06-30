#!/usr/bin/env python3
"""
FUGUEJUKEBOX: Atalanta Fugiens Chiptune Variations Generator

Transforms the 50 Atalanta Fugiens fugues into 10 NES-inspired experimental
variations per emblem. Uses synthesizer sounds, harmonic elaboration, scale runs,
and effects (reverb, vibrato, delay) to voice each fugue as a Nintendo soundtrack.

Pipeline:
  1. Load fugues.json (MIDI note data for 50 emblems)
  2. Extract NES sounds from game libraries via NSFRipper
  3. Generate 10 variations per emblem:
     - Variation 1-3: Harmonic voicings (root position, inversions, extended chords)
     - Variation 4-6: Scale runs & improvisations (diatonic runs, chromatic fills)
     - Variation 7-10: Effect treatments (reverb, vibrato/tremolo, delay/echo chains)
  4. Render each variation to WAV using Web Audio synthesis + effects
  5. Export to MP3 in FUGUEJUKEBOX/emblems/{emblem_num}/
"""

import json
import os
import sys
from pathlib import Path
from typing import Dict, List, Tuple
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)
log = logging.getLogger(__name__)

# Paths
PROJECT_ROOT = Path(__file__).parent
EMBLEMROGUELIKE_ROOT = Path("C:/Dev/EmblemRoguelike")
FUGUES_JSON = EMBLEMROGUELIKE_ROOT / "assets" / "fugues.json"
NSF_LIBRARY = Path("C:/Dev/NESjamtools/assets/nsf")
OUTPUT_DIR = PROJECT_ROOT / "emblems"
SOUNDS_DIR = PROJECT_ROOT / "sounds"
METADATA_DIR = PROJECT_ROOT / "metadata"

# MIDI pitch constants
MIDDLE_C = 60
A4 = 69

def load_fugues() -> Dict[str, Dict]:
    """Load the 50 Atalanta Fugiens fugues from fugues.json."""
    if not FUGUES_JSON.exists():
        log.error(f"fugues.json not found at {FUGUES_JSON}")
        return {}

    with open(FUGUES_JSON, 'r') as f:
        fugues = json.load(f)

    log.info(f"Loaded {len(fugues)} fugues from {FUGUES_JSON}")
    return fugues


def generate_harmonic_variations(notes: List[List[float]]) -> List[List[List[float]]]:
    """
    Generate 3 harmonic variations from original monophonic line:
    1. Root position harmony (add 3rd + 5th)
    2. First inversion (add 6th + octave)
    3. Close voicing (triadic stacks)
    """
    base_pitch = notes[0][2] if notes else MIDDLE_C

    # Build simple 3-voice harmony
    var1 = []  # Root position
    var2 = []  # First inversion
    var3 = []  # Close voicing

    for start, dur, midi in notes:
        # Base melody
        var1.append([start, dur, midi])
        var2.append([start, dur, midi])
        var3.append([start, dur, midi])

        # Add harmony voices (thirds and fifths)
        # Var 1: add third below, fifth below
        var1.append([start, dur, midi - 4])  # major third
        var1.append([start, dur, midi - 7])  # perfect fifth

        # Var 2: first inversion voicing
        var2.append([start, dur, midi - 3])  # minor third
        var2.append([start, dur, midi + 5])  # major sixth above

        # Var 3: close voicing (all within octave)
        var3.append([start, dur, midi - 2])  # whole step below
        var3.append([start, dur, midi + 3])  # minor third above

    return [var1, var2, var3]


def generate_run_variations(notes: List[List[float]], bpm: float) -> List[List[List[float]]]:
    """
    Generate 3 scale-run variations:
    1. Diatonic scalar runs filling large intervals
    2. Chromatic approach notes
    3. Arpeggio-based fills
    """
    # Define C major scale for now (can extract key from melody)
    DIATONIC = [0, 2, 4, 5, 7, 9, 11]  # semitone offsets

    var4 = []  # Diatonic runs
    var5 = []  # Chromatic approach
    var6 = []  # Arpeggios

    base_octave = MIDDLE_C

    for i, (start, dur, midi) in enumerate(notes):
        # Original note
        var4.append([start, dur, midi])
        var5.append([start, dur, midi])
        var6.append([start, dur, midi])

        # Add runs on longer notes (dur > 1 beat)
        if dur > 1.0:
            fill_dur = dur / 3

            # Var 4: diatonic run downward
            for j in range(1, 3):
                scale_step = DIATONIC[j % len(DIATONIC)]
                var4.append([start + j * fill_dur, fill_dur, midi - scale_step])

            # Var 5: chromatic approach from above
            for j in range(1, 3):
                var5.append([start + j * fill_dur, fill_dur, midi + (3 - j)])

            # Var 6: arpeggio pattern
            for j in range(1, 3):
                arp_pitch = midi - 7 + (j * 4)  # 5th, major 7th pattern
                var6.append([start + j * fill_dur, fill_dur, arp_pitch])

    return [var4, var5, var6]


def generate_effect_variations(notes: List[List[float]], bpm: float) -> List[Dict]:
    """
    Generate 4 effect-based variations with metadata for Web Audio processing:
    1. Heavy reverb (cathedral/spacious)
    2. Vibrato/tremolo (wobble effect)
    3. Delay/echo cascade
    4. Combination (reverb + vibrato + gentle delay)
    """
    effects = [
        {
            'name': 'Cathedral Reverb',
            'reverb_wet': 0.7,
            'reverb_decay': 2.5,
            'reverb_early_reflections': True,
            'delay_wet': 0.0,
            'vibrato_depth': 0.0
        },
        {
            'name': 'Vibrato Wobble',
            'reverb_wet': 0.2,
            'reverb_decay': 1.0,
            'delay_wet': 0.0,
            'vibrato_depth': 0.15,
            'vibrato_rate': 5.5,  # Hz
            'tremolo_depth': 0.1,
            'tremolo_rate': 3.0
        },
        {
            'name': 'Echo Cascade',
            'reverb_wet': 0.1,
            'delay_wet': 0.6,
            'delay_times': [0.375, 0.75, 1.125],  # triplet rhythms
            'delay_feedback': 0.5,
            'vibrato_depth': 0.0
        },
        {
            'name': 'Spacious Chorus',
            'reverb_wet': 0.5,
            'reverb_decay': 1.8,
            'delay_wet': 0.2,
            'delay_times': [0.5],
            'vibrato_depth': 0.08,
            'vibrato_rate': 4.2,
            'tremolo_depth': 0.05,
            'tremolo_rate': 2.0
        }
    ]

    # Attach the original notes to each effect config
    for effect in effects:
        effect['notes'] = notes

    return effects


def create_emblem_variations(emblem_num: int, fugue_data: Dict) -> Dict:
    """
    Create all 10 variations for a single emblem.
    Returns metadata about generated variations.
    """
    notes = fugue_data.get('notes', [])
    bpm = fugue_data.get('bpm', 75)
    beats = fugue_data.get('beats', 0)

    if not notes:
        log.warning(f"Emblem {emblem_num}: no notes found, skipping")
        return {}

    log.info(f"Emblem {emblem_num:2d}: generating 10 variations ({len(notes)} notes, {bpm} bpm, {beats:.1f} beats)")

    # Generate variations
    harmonic = generate_harmonic_variations(notes)
    runs = generate_run_variations(notes, bpm)
    effects = generate_effect_variations(notes, bpm)

    # Build variation metadata
    variations = []

    # Harmonic variations (1-3)
    for i, var_notes in enumerate(harmonic, 1):
        variations.append({
            'variation_num': i,
            'category': 'harmonic',
            'name': ['Root Position Harmony', 'First Inversion Voicing', 'Close Voicing'][i-1],
            'notes': var_notes,
            'bpm': bpm,
            'beats': beats,
            'effects': {}
        })

    # Run variations (4-6)
    for i, var_notes in enumerate(runs, 1):
        variations.append({
            'variation_num': i + 3,
            'category': 'runs',
            'name': ['Diatonic Scalar Runs', 'Chromatic Approach Notes', 'Arpeggio Fills'][i-1],
            'notes': var_notes,
            'bpm': bpm,
            'beats': beats,
            'effects': {}
        })

    # Effect variations (7-10)
    for i, effect_config in enumerate(effects, 1):
        var_notes = effect_config.pop('notes')
        variations.append({
            'variation_num': i + 6,
            'category': 'effects',
            'name': f"Variation 7-10 ({effect_config.get('name', 'Unknown')})",
            'notes': var_notes,
            'bpm': bpm,
            'beats': beats,
            'effects': effect_config
        })

    return {
        'emblem': emblem_num,
        'original_notes': len(notes),
        'bpm': bpm,
        'beats': beats,
        'variations': variations
    }


def main():
    log.info("=== FUGUEJUKEBOX: Atalanta Fugiens Chiptune Variations ===")

    # Load fugues
    fugues = load_fugues()
    if not fugues:
        log.error("No fugues loaded, exiting")
        sys.exit(1)

    # Generate variations for each emblem
    all_metadata = {}

    for emblem_num in sorted(int(k) for k in fugues.keys()):
        fugue_data = fugues[str(emblem_num)]
        emblem_meta = create_emblem_variations(emblem_num, fugue_data)

        if emblem_meta:
            all_metadata[emblem_num] = emblem_meta

            # Create emblem-specific directory
            emblem_dir = OUTPUT_DIR / f"emblem_{emblem_num:02d}"
            emblem_dir.mkdir(parents=True, exist_ok=True)

            # Save variation metadata to JSON
            meta_file = emblem_dir / "variations.json"
            with open(meta_file, 'w') as f:
                json.dump(emblem_meta, f, indent=2)

            log.info(f"  → Saved metadata: {meta_file}")

    # Save global metadata
    global_meta_file = METADATA_DIR / "all_variations.json"
    with open(global_meta_file, 'w') as f:
        json.dump(all_metadata, f, indent=2)

    log.info(f"\n✓ Generated variations for {len(all_metadata)} emblems")
    log.info(f"✓ Total variations: {len(all_metadata) * 10}")
    log.info(f"✓ Output directory: {OUTPUT_DIR}")
    log.info(f"✓ Metadata: {global_meta_file}")
    log.info("\nNext: Run render_to_audio.py to synthesize and export MP3s")


if __name__ == '__main__':
    main()
