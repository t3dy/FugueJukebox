'use client'

import Link from 'next/link'
import { Music, Zap, Flame } from 'lucide-react'
import emblems from '@/data/emblems.json'

export default function Home() {
  const totalVariations = 500
  const totalEmblems = 50

  return (
    <main className="flex-1">
      {/* Header/Navigation */}
      <header className="border-b border-slate-700 sticky top-0 bg-slate-950/80 backdrop-blur-md z-50">
        <nav className="container py-4 flex items-center justify-between">
          <Link href="/" className="text-2xl font-bold gradient-text">
            FUGUEJUKEBOX
          </Link>
          <div className="flex gap-6 items-center">
            <Link href="/" className="hover:text-slate-200 transition">Home</Link>
            <Link href="#emblems" className="hover:text-slate-200 transition">Emblems</Link>
            <Link href="#about" className="hover:text-slate-200 transition">About</Link>
          </div>
        </nav>
      </header>

      {/* Hero Section */}
      <section className="container py-20 text-center">
        <h1 className="mb-6">FUGUEJUKEBOX</h1>
        <p className="text-xl max-w-2xl mx-auto mb-8">
          Fifty alchemical emblems. Ten musical variations each. Five hundred chiptune compositions.
        </p>
        <p className="text-lg text-slate-400 max-w-3xl mx-auto mb-12">
          Michael Maier's <em>Atalanta Fugiens</em> (1617) transformed into Nintendo-inspired music.
          Harmonic elaborations, scalar improvisations, and digital effects—a complete sonic journey
          through the Great Work.
        </p>

        <div className="grid grid-cols-3 gap-8 max-w-2xl mx-auto mb-12">
          <div className="card text-center">
            <Music className="w-8 h-8 mx-auto mb-4 text-amber-500" />
            <div className="text-3xl font-bold gradient-text mb-2">{totalEmblems}</div>
            <p className="text-sm">Emblems</p>
          </div>
          <div className="card text-center">
            <Zap className="w-8 h-8 mx-auto mb-4 text-amber-500" />
            <div className="text-3xl font-bold gradient-text mb-2">10</div>
            <p className="text-sm">Variations Each</p>
          </div>
          <div className="card text-center">
            <Flame className="w-8 h-8 mx-auto mb-4 text-amber-500" />
            <div className="text-3xl font-bold gradient-text mb-2">{totalVariations}</div>
            <p className="text-sm">MP3 Files</p>
          </div>
        </div>

        <Link href="/#emblems" className="btn">
          Browse Emblems
        </Link>
      </section>

      {/* About Section */}
      <section id="about" className="bg-slate-900/50 py-16 border-y border-slate-700">
        <div className="container max-w-3xl">
          <h2 className="mb-8">About This Project</h2>

          <div className="space-y-6">
            <div>
              <h3 className="text-amber-500 mb-3">The Source</h3>
              <p>
                <em>Atalanta Fugiens</em> (1617) by Michael Maier is a multimedia alchemical work
                comprising fifty emblems, each pairing an engraved plate, Latin motto, three-voice
                fugue, epigram, and discourse. It encodes the stages of the alchemical opus
                (the Great Work) through sophisticated synthesis of Hermetic, classical, and
                biblical traditions.
              </p>
            </div>

            <div>
              <h3 className="text-amber-500 mb-3">The Transformation</h3>
              <p>
                FUGUEJUKEBOX reimagines Maier's fugues as chiptune compositions. The 50 three-voice
                canons become 500 variations:
              </p>
              <ul className="list-disc list-inside space-y-2 mt-3">
                <li><strong>Harmonic Elaborations (1-3):</strong> Root position, inversions, close voicings</li>
                <li><strong>Scale Runs (4-6):</strong> Diatonic runs, chromatic approaches, arpeggios</li>
                <li><strong>Effect Treatments (7-10):</strong> Cathedral reverb, vibrato wobble, echo cascade, spacious chorus</li>
              </ul>
            </div>

            <div>
              <h3 className="text-amber-500 mb-3">The Sound</h3>
              <p>
                Square-wave NES-style synthesis (44.1 kHz, 16-bit PCM, MP3 @ 192 kbps).
                Each file is ~34 seconds—the time to listen deeply while reading Maier's epigrams and contemplating
                the alchemical transformation they encode.
              </p>
            </div>

            <div>
              <h3 className="text-amber-500 mb-3">How to Listen</h3>
              <p>
                <strong>By Emblem:</strong> Start with any emblem and play all 10 variations to hear the same melody
                transformed through harmony, improvisation, and effects.
              </p>
              <p className="mt-2">
                <strong>By Category:</strong> Listen to all "Cathedral Reverb" tracks for a meditative experience,
                or "Scalar Runs" for rhythmic energy.
              </p>
              <p className="mt-2">
                <strong>As a Journey:</strong> Follow emblems 1-50 in order to trace the progression from
                Nigredo (blackening) through Albedo (whitening) to Rubedo (reddening)—the complete Great Work.
              </p>
            </div>
          </div>

          <div className="divider"></div>

          <p className="text-sm text-slate-400">
            <strong>Public Domain.</strong> These works derive from Maier's <em>Atalanta Fugiens</em> (1617),
            and are free to use, modify, and share. Attribution appreciated.
          </p>
        </div>
      </section>

      {/* Emblems Section */}
      <section id="emblems" className="container py-20">
        <h2 className="mb-12 text-center">The 50 Emblems</h2>

        <div className="grid grid-cols-3 gap-6">
          {emblems.emblems.map((emblem) => (
            <Link
              key={emblem.id}
              href={`/emblem/${emblem.id}`}
              className="card group"
            >
              <div className="flex items-start justify-between mb-4">
                <div>
                  <div className="text-sm text-slate-400 font-mono">{emblem.roman}</div>
                  <h3 className="group-hover:text-amber-400 transition">{emblem.title}</h3>
                </div>
              </div>
              <p className="text-sm text-slate-400 italic line-clamp-2">
                "{emblem.epigram}"
              </p>
              <div className="mt-4 pt-4 border-t border-slate-700">
                <span className="inline-block px-2 py-1 text-xs bg-slate-800 rounded">
                  {emblem.phase_name}
                </span>
              </div>
            </Link>
          ))}
        </div>
      </section>

      {/* Footer */}
      <footer className="border-t border-slate-700 bg-slate-900/50 py-12 mt-20">
        <div className="container max-w-3xl">
          <div className="grid grid-cols-auto gap-12 mb-8">
            <div>
              <h4 className="font-bold mb-4">Navigation</h4>
              <ul className="space-y-2">
                <li><Link href="/" className="hover:text-amber-400">Home</Link></li>
                <li><Link href="/#emblems" className="hover:text-amber-400">Emblems</Link></li>
              </ul>
            </div>
            <div>
              <h4 className="font-bold mb-4">Resources</h4>
              <ul className="space-y-2">
                <li><a href="#" className="hover:text-amber-400">Learn More</a></li>
                <li><a href="#" className="hover:text-amber-400">Source Texts</a></li>
              </ul>
            </div>
          </div>

          <div className="divider"></div>

          <p className="text-sm text-slate-500 text-center">
            FUGUEJUKEBOX © 2026 | Based on Michael Maier's <em>Atalanta Fugiens</em> (1617)
            <br />
            Made with Python, scipy, ffmpeg, and Claude Code
          </p>
        </div>
      </footer>
    </main>
  )
}
