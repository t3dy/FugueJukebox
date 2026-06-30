# FUGUEJUKEBOX Website

A dark academic website showcasing 50 Atalanta Fugiens emblems with 500 playable chiptune musical variations.

## Features

- **Home Page:** Overview of the project with statistics and listening guide
- **Emblem Index:** All 50 emblems browsable as cards
- **Emblem Detail Pages:** Individual emblem pages with:
  - Emblem title, number, and Roman numeral
  - Epigram (call to action)
  - Poem (theme summary)
  - Alchemical phase (Nigredo, Albedo, Citrinitas, Rubedo)
  - 10 playable MP3s (3 harmonic + 3 runs + 4 effects)
  - Descriptions of each variation type
  - Navigation to previous/next emblems

- **Responsive Design:** Dark theme optimized for long reading/listening sessions
- **Audio Players:** Built-in browser audio controls for each variation

## Setup

### Prerequisites

- Node.js 18+ (LTS)
- npm or yarn

### Installation

```bash
cd FUGUEJUKEBOX-website

# Install dependencies
npm install

# Run development server
npm run dev

# Build for production
npm build
npm start
```

The site will be available at `http://localhost:3000`

## Project Structure

```
FUGUEJUKEBOX-website/
├── app/
│   ├── layout.tsx           # Root layout with HTML/head
│   ├── globals.css          # Global styles (dark academic theme)
│   ├── page.tsx             # Home page
│   └── emblem/
│       └── [id]/
│           └── page.tsx     # Emblem detail page
├── data/
│   └── emblems.json         # All 50 emblems with metadata
├── public/                  # Static assets (future)
├── package.json
├── tsconfig.json
├── next.config.ts
└── README.md
```

## Data Format

Each emblem in `data/emblems.json` contains:

```json
{
  "id": 1,
  "roman": "I",
  "title": "His Nurse is the Earth",
  "epigram": "The philosophical child must be nurtured by the earth-mother.",
  "poem": "The infant stone seeks mother earth...",
  "phase": "foundation",
  "phase_name": "Nigredo"
}
```

## Audio Files

MP3 files are referenced from the FUGUEJUKEBOX project directory:

```
../../../FUGUEJUKEBOX/emblems/emblem_XX/emblem_XX_variation_YY.mp3
```

Make sure the FUGUEJUKEBOX directory with all 500 MP3s is in place before running the site.

## Variation Categories

### 1-3: Harmonic Elaborations
- Root Position Harmony
- First Inversion Voicing
- Close Voicing

### 4-6: Scale Runs & Improvisations
- Diatonic Scalar Runs
- Chromatic Approach Notes
- Arpeggio Fills

### 7-10: Effect Treatments
- Cathedral Reverb (70% wet, 2.5s decay)
- Vibrato Wobble (LFO + tremolo)
- Echo Cascade (triplet delays, feedback)
- Spacious Chorus (combined effects)

## Styling

The site uses a dark academic aesthetic:

- **Font:** EB Garamond (serif) for body, Inter for UI
- **Colors:** Slate-950 background, slate-100 text, amber-600 accents
- **Theme:** Inspired by scholarly journal design with musical elements

CSS custom properties defined in `globals.css`:
- `--color-bg-dark`: #0f172a
- `--color-text-primary`: #f1f5f9
- `--color-accent-gold`: #d4af37

## Development

### Tailwind CSS

This project uses a custom CSS approach (not Tailwind). Utility classes are defined in `globals.css`.

### Adding New Pages

1. Create a new folder in `app/`
2. Add `page.tsx` with React component
3. Use the `container` class for max-width layout
4. Import emblem data as needed

### Modifying Emblem Data

Edit `data/emblems.json` to update emblem information. The site will automatically reflect changes.

## Deployment

### Static Export

Generate a static HTML export:

```bash
npm run build
npm run export  # (add to package.json if needed)
```

### Vercel

Deploy directly to Vercel:

```bash
npx vercel
```

### GitHub Pages

Configure for GitHub Pages deployment in `next.config.ts`.

## Performance

- No external dependencies (except React/Next)
- All assets served locally
- Optimized CSS (single global stylesheet)
- Fast page transitions with Next.js routing

## Browser Support

- Modern browsers (Chrome, Firefox, Safari, Edge)
- Audio element support required for playback
- CSS Grid and Flexbox for layout

## Future Enhancements

- [ ] Emblem artwork/images
- [ ] Full Maier texts and translations
- [ ] Playlist builder (save favorite variations)
- [ ] Dark/light mode toggle
- [ ] Search by emblem title or number
- [ ] Export playlists as M3U
- [ ] Integration with EmblemRoguelike game

## License

Public Domain. Based on Michael Maier's *Atalanta Fugiens* (1617).

---

**Made with:** Next.js, React, TypeScript, and Claude Code

**Project:** FUGUEJUKEBOX © 2026
