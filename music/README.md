# FUGUEJUKEBOX: Atalanta Fugiens Chiptune Variations

**A Nintendo-inspired musical interpretation of the 50 Atalanta Fugiens emblems.**

Generated June 29, 2026 | 500 MP3 files | ~130 MB total

---

## What This Is

This project transforms Michael Maier's *Atalanta Fugiens* (1617)—50 three-voice alchemical canons—into experimental NES-style chiptune variations. Each emblem gets 10 unique instrumental treatments:

- **Variations 1-3:** Harmonic Elaborations (root position, inversions, close voicings)
- **Variations 4-6:** Scale Runs & Improvisations (diatonic runs, chromatic fills, arpeggios)
- **Variations 7-10:** Effect Treatments (cathedral reverb, vibrato wobble, echo cascade, spacious chorus)

Each file is synthesized using square-wave NES-style synthesis (like the original *Atalanta Fugiens* appears in the EmblemRoguelike game), with layered harmonies and digital effects.

---

## Structure

```
FUGUEJUKEBOX/
├── emblems/                    # Output folder (all 500 MP3s)
│   ├── emblem_01/
│   │   ├── emblem_01_variation_01.mp3   (Root Position Harmony)
│   │   ├── emblem_01_variation_02.mp3   (First Inversion Voicing)
│   │   ├── emblem_01_variation_03.mp3   (Close Voicing)
│   │   ├── emblem_01_variation_04.mp3   (Diatonic Scalar Runs)
│   │   ├── emblem_01_variation_05.mp3   (Chromatic Approach Notes)
│   │   ├── emblem_01_variation_06.mp3   (Arpeggio Fills)
│   │   ├── emblem_01_variation_07.mp3   (Cathedral Reverb)
│   │   ├── emblem_01_variation_08.mp3   (Vibrato Wobble)
│   │   ├── emblem_01_variation_09.mp3   (Echo Cascade)
│   │   ├── emblem_01_variation_10.mp3   (Spacious Chorus)
│   │   └── variations.json
│   ├── emblem_02/
│   ├── ...
│   └── emblem_50/
│
├── metadata/
│   └── all_variations.json     # Complete variation metadata
│
├── build_logs/                 # Generation and rendering logs
│
├── generate_variations.py      # Step 1: Generate variation note data
├── render_to_audio.py          # Step 2: Synthesize to MP3
├── build_all.py                # Orchestration script
└── README.md                   # This file
```

---

## Listening Guide

### By Emblem (Sample)

| Emblem | Title | Variations Link |
|--------|-------|-----------------|
| 1 | His Nurse is the Earth | `emblem_01/` |
| 3 | Go to the Woman Who Washes | `emblem_03/` |
| 5 | The Toad Bearing Its Chain | `emblem_05/` |
| 7 | Balance the Winged and Wingless Birds | `emblem_07/` |
| 21 | The Philosopher's Stone | `emblem_21/` |
| 42 | The Hermaphrodite in Darkness | `emblem_42/` |
| 50 | Osiris Sleeps (Conclusion) | `emblem_50/` |

### By Variation Category

**Harmonic Variations** → Listen to variations 1-3 from any emblem for chord-based reharmonization.

**Scale Runs** → Listen to variations 4-6 for scalar improvisation and arpeggio fills.

**Effects** → Listen to variations 7-10 for the full digital treatment:
- **Variation 7 (Cathedral Reverb):** Spacious, ecclesiastical reverb (2.5s decay)
- **Variation 8 (Vibrato Wobble):** Tremolo + vibrato (5.5 Hz wobble rate)
- **Variation 9 (Echo Cascade):** Triplet-rhythm delays with feedback
- **Variation 10 (Spacious Chorus):** Combined reverb + gentle vibrato + delay

---

## Technical Details

### Synthesis
- **Waveform:** Square wave (NES-like tones)
- **Sample rate:** 44,100 Hz
- **Bit depth:** 16-bit PCM (MP3 @ 192 kbps)
- **ADSR Envelope:** 15ms attack, 100ms release per note

### Data Source
- **Original fugues:** EmblemRoguelike/assets/fugues.json (parsed from MIDI scores)
- **Emblem data:** 50 three-voice canons, 44-79 beats each, BPM range 50-80
- **Total notes:** ~5,000 across all emblems

### Effects Processing
- **Reverb:** Exponential decay impulse convolution (1.5-2.5s decay)
- **Vibrato/Tremolo:** Sine LFO at 3-5.5 Hz depth
- **Delay:** Multi-tap feedback (triplet rhythms at 375/750/1125ms)
- **Normalization:** Prevents clipping, maintains 1.05x headroom

---

## Generation Pipeline

```bash
# Step 1: Generate variation data (note sequences + effect configs)
python generate_variations.py
# → Creates 50 emblem_XX/ directories with variations.json metadata

# Step 2: Render to audio (synthesize + apply effects)
python render_to_audio.py
# → Synthesizes each variation to WAV, converts to MP3

# Or run both at once:
python build_all.py
```

---

## Files Generated

- **500 MP3 files** (~130 MB total, ~260 KB per file)
- **50 metadata files** (variations.json, one per emblem)
- **1 global index** (all_variations.json)
- **Build logs** (generation and rendering logs)

---

## Next Steps

1. **Listen:** Open any emblem folder and sample the 10 variations
2. **Curate:** Select your favorite treatments per emblem
3. **Combine:** Stack variations into themed playlists (e.g., "Ceremonial Alchemy," "Chaotic Digestion," "Silent Transmutation")
4. **Integrate:** Use these in the EmblemRoguelike game or a standalone music player

---

## Sources & Attribution

- **Original Atalanta Fugiens:** Michael Maier, 1617 (50 emblem fugues, public domain)
- **MIDI sequencings:** Parsed from EmblemRoguelike project
- **Alchemical themes:** Each emblem corresponds to a stage in the Great Work (Nigredo, Albedo, Citrinitas, Rubedo)

---

## Metadata Format

Each `emblem_XX/variations.json` contains:

```json
{
  "emblem": 1,
  "original_notes": 115,
  "bpm": 75,
  "beats": 44,
  "variations": [
    {
      "variation_num": 1,
      "category": "harmonic",
      "name": "Root Position Harmony",
      "notes": [[start_beat, dur_beat, midi], ...],
      "bpm": 75,
      "beats": 44,
      "effects": {}
    },
    ...
    {
      "variation_num": 7,
      "category": "effects",
      "name": "Variation 7-10 (Cathedral Reverb)",
      "notes": [...],
      "bpm": 75,
      "beats": 44,
      "effects": {
        "reverb_wet": 0.7,
        "reverb_decay": 2.5,
        "delay_wet": 0.0,
        "vibrato_depth": 0.0
      }
    }
  ]
}
```

---

## License & Usage

These files are derived from the public-domain *Atalanta Fugiens* (1617) and are free to use, modify, and share. Attribution appreciated but not required.

Use for:
- Listening & curation
- Game soundtracks
- Meditation / study music
- Alchemical atmosphere
- Experimental music projects

---

**Made with Claude Code** | 2026
