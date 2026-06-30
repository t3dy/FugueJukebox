# FUGUEJUKEBOX

Atalanta Fugiens (1617) by Michael Maier transformed into 500 chiptune musical variations with a dark academic website for browsing and listening.

**🌐 Live Website:** 
- **⭐ [https://fuguejukebox.vercel.app](https://fuguejukebox.vercel.app)** ← **LIVE ON THE WEB!**
- **Local Development:** http://localhost:3001 (after running `npm run dev`)

## 🎵 Projects

- **[website/](website/)** — 🌐 **[Live Website](http://localhost:3001)** — React/Next.js dark academic website with playable audio embeds
- **[music/](music/)** — 500 NES-style chiptune MP3s (50 emblems × 10 variations each)

## 🚀 Quick Start

### Website
```bash
cd website
npm install
npm run dev
```
**→ Open http://localhost:3001 in your browser**

**Deploy to Vercel:**
```bash
cd website
vercel
```

### Music Files
All 500 MP3 files organized in:
```
music/emblems/
├── emblem_01/
│   ├── emblem_01_variation_01-10.mp3
│   └── variations.json
├── emblem_02/
...
└── emblem_50/
```

## 📚 Documentation

### Music Project
- [music/README.md](music/README.md) — Project overview and listening guide
- [music/MANIFEST.md](music/MANIFEST.md) — Complete generation report & statistics
- [music/CATALOG.md](music/CATALOG.md) — All 50 emblems listed with descriptions

### Website Project
- [website/README.md](website/README.md) — Setup and development guide
- [website/LAUNCH.md](website/LAUNCH.md) — Deployment and technical details

## ✨ Features

### Music
✅ 500 chiptune variations (50 emblems × 10 each)  
✅ 3 harmonic elaborations per emblem  
✅ 3 scalar improvisation variations per emblem  
✅ 4 digital effect treatments per emblem  
✅ NES-style square wave synthesis  
✅ High-quality audio (44.1 kHz, 16-bit, 192 kbps MP3)  

### Website
✅ Home page with project overview  
✅ Complete emblem index (50 cards)  
✅ Individual emblem detail pages  
✅ 10 playable MP3 players per emblem  
✅ Emblem metadata (epigram, poem, alchemical phase)  
✅ Dark academic aesthetic (EB Garamond, slate/gold)  
✅ Full navigation (prev/next, back to index)  
✅ Responsive design (desktop + mobile)  
✅ Built-in audio controls  

## 📊 Statistics

- **Total Variations:** 500
- **Total File Size:** ~140 MB
- **Average Per MP3:** ~293 KB, ~34 seconds
- **Format:** 44.1 kHz, 16-bit PCM, 192 kbps MP3
- **Emblems:** 50
- **Variations Per Emblem:** 10

## 🎯 Variation Types

### Harmonic Elaborations (1-3)
- Root Position Harmony
- First Inversion Voicing
- Close Voicing

### Scale Runs & Improvisations (4-6)
- Diatonic Scalar Runs
- Chromatic Approach Notes
- Arpeggio Fills

### Effect Treatments (7-10)
- Cathedral Reverb (70% wet, 2.5s decay)
- Vibrato Wobble (LFO + tremolo)
- Echo Cascade (triplet delays, feedback)
- Spacious Chorus (combined effects)

## 🔧 Technical Stack

**Music Generation:**
- Python 3
- scipy (audio synthesis & effects)
- ffmpeg (MP3 encoding)

**Website:**
- React 18
- Next.js 14
- TypeScript 5
- CSS (custom, no Tailwind)
- HTML5 Audio element

## 📖 About the Source

*Atalanta Fugiens* (1617) is a multimedia alchemical emblem book by Michael Maier comprising 50 emblems, each combining:
- An engraved plate
- A Latin motto
- A three-voice fugue
- A Latin epigram
- A two-page Latin discourse

FUGUEJUKEBOX reimagines these 50 fugues as chiptune compositions with harmonic, improvisational, and digital effect treatments.

## 📜 License

**Public Domain.** Based on Michael Maier's *Atalanta Fugiens* (1617), a public-domain work.

Free to use, modify, and distribute. Attribution appreciated:

> FUGUEJUKEBOX © 2026 | Based on *Atalanta Fugiens* by Michael Maier (1617) | Made with Python, Next.js, and Claude Code

## 🔗 Links & Resources

**Website:**
- 🌐 **[Live Website](https://fuguejukebox.vercel.app)** — **LIVE! Click to browse emblems and listen to music**
- 🏠 **[Local Development](http://localhost:3001)** — Visit after running `npm run dev`
- 📖 **[Website Documentation](website/README.md)** — Setup and development guide
- 🚀 **[Deployment Guide](website/LAUNCH.md)** — Vercel deployment instructions

**Music:**
- 🎵 **[Music Project](music/)** — Generation scripts and emblem metadata
- 📚 **[Music Documentation](music/README.md)** — Overview and listening guide
- 📋 **[Emblem Catalog](music/CATALOG.md)** — All 50 emblems listed

**Repository:**
- 📦 **[GitHub Repository](https://github.com/t3dy/FugueJukebox)** — Source code
- 📝 **[Deployment Guide](DEPLOYMENT.md)** — Clone and deployment instructions

## 📝 Credits

- **Music Source:** Michael Maier's *Atalanta Fugiens* (1617)
- **MIDI Data:** EmblemRoguelike project
- **Synthesis & Effects:** Python audio pipeline
- **Website:** React/Next.js
- **Created:** 2026-06-29

---

**Status:** ✅ Complete and Operational  
**Last Updated:** 2026-06-29
