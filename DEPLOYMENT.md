# Deployment Guide

## GitHub Repository

**FUGUEJUKEBOX** is now deployed to GitHub at:
- **Repository URL:** https://github.com/t3dy/FugueJukebox
- **Status:** Public and Live
- **Branch:** main

## What's in the Repository

### Website Project (`website/`)
- **Framework:** React 18 + Next.js 14 + TypeScript
- **Styling:** Custom CSS (dark academic aesthetic)
- **Components:** Home page + 50 emblem detail pages
- **Data:** Emblem metadata JSON
- **Scripts:** Package.json with dev/build commands
- **Docs:** README.md and LAUNCH.md

### Music Project (`music/`)
- **Scripts:** Python generation and rendering pipelines
- **Documentation:** README, MANIFEST, CATALOG
- **Metadata:** Complete variation metadata JSON
- **Status:** Scripts ready to regenerate MP3s

### Documentation (`/`)
- **README.md** — Project overview and quick start
- **DEPLOYMENT.md** — This file
- **.gitignore** — Excludes build artifacts and large files

## What's NOT in the Repository

### MP3 Audio Files (140 MB)
The 500 MP3 files are **not included** in the GitHub repository because:
1. GitHub has file size limits (100 MB hard limit per file)
2. Repository size recommendations (< 1 GB total)
3. Large binaries impact cloning speed

**Location:** `C:\Dev\FUGUEJUKEBOX\emblems\` (local storage)

**Option for future inclusion:**
- Use **Git LFS** (Large File Storage) to add MP3s to the repository
- Document will be updated if LFS is set up

## Cloning and Running Locally

### Clone the Repository
```bash
git clone https://github.com/t3dy/FugueJukebox.git
cd FugueJukebox
```

### Run the Website
```bash
cd website
npm install
npm run dev
# Visit http://localhost:3001
```

### Generate Music Files (Optional)
Requires Python 3 with scipy, numpy, and ffmpeg:

```bash
cd music

# Generate variations (metadata)
python generate_variations.py

# Render to audio (MP3s)
python render_to_audio.py

# Or do both at once
python build_all.py
```

## Project Structure
```
FugueJukebox/
├── README.md              # Project overview
├── DEPLOYMENT.md          # This file
├── .gitignore            # Git ignore rules
├── website/              # React/Next.js website
│   ├── app/             # React app code
│   ├── data/            # Emblem metadata
│   ├── package.json
│   ├── README.md
│   └── LAUNCH.md
└── music/               # Audio generation scripts
    ├── generate_variations.py
    ├── render_to_audio.py
    ├── build_all.py
    ├── README.md
    ├── MANIFEST.md
    ├── CATALOG.md
    └── metadata/
```

## Commits

| Hash | Message |
|------|---------|
| `fa1165b` | Add website and music source code |
| `2a2673d` | Initial commit: FUGUEJUKEBOX project structure |

## Technology Stack

**Website:**
- React 18
- Next.js 14
- TypeScript 5
- Custom CSS

**Music Generation:**
- Python 3
- scipy (audio synthesis)
- ffmpeg (MP3 encoding)

**Deployment:**
- GitHub (source control)
- Vercel (recommended for website hosting)
- Local storage for MP3s

## Future Enhancement Ideas

- [ ] Add Git LFS for MP3 files
- [ ] Deploy website to Vercel
- [ ] Add CI/CD pipeline
- [ ] Set up GitHub Actions for builds
- [ ] Add GitHub Pages for project site
- [ ] Docker containerization for website
- [ ] Add unit tests for website
- [ ] Add audio playback tests

## Contributing

This repository is public. Contributions are welcome!

### To Contribute:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

### Areas for Contribution:
- Website enhancements
- New variation techniques
- Better documentation
- Optimization ideas
- Bug fixes

## License

**Public Domain.** Based on Michael Maier's *Atalanta Fugiens* (1617).

Free to use, modify, and distribute.

## Support

- **Issues:** https://github.com/t3dy/FugueJukebox/issues
- **Discussions:** https://github.com/t3dy/FugueJukebox/discussions
- **Email:** ted.hand@gmail.com

## Deployment Status

✅ **Repository:** Created and pushed to GitHub  
✅ **Website Code:** Published  
✅ **Documentation:** Complete  
⏳ **MP3 Files:** Local storage (can be added via Git LFS)  
⏳ **Website Hosting:** Ready for Vercel deployment  

## Next Steps

1. **Clone and test locally:**
   ```bash
   git clone https://github.com/t3dy/FugueJukebox.git
   ```

2. **Deploy website to Vercel:**
   ```bash
   cd website
   vercel
   ```

3. **Set up Git LFS (optional):**
   ```bash
   git lfs install
   git lfs track "music/emblems/**/*.mp3"
   git add .gitattributes
   git commit -m "Set up Git LFS for MP3 files"
   git push
   ```

4. **Open issues or discussions** for feature requests or bug reports

---

**Deployment Date:** 2026-06-29  
**Repository:** https://github.com/t3dy/FugueJukebox  
**Status:** ✅ Live and Operational
