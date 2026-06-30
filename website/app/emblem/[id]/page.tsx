'use client'

import { useState } from 'react'
import Link from 'next/link'
import { ChevronLeft, ChevronRight, Volume2 } from 'lucide-react'
import emblems from '@/data/emblems.json'

const VARIATION_DESCRIPTIONS = {
  1: 'Root Position Harmony — Triadic harmony with thirds and fifths below the melody',
  2: 'First Inversion Voicing — Reposition voices for flowing counterpoint',
  3: 'Close Voicing — All voices within a single octave for compact texture',
  4: 'Diatonic Scalar Runs — Fill intervals with stepwise motion in C major',
  5: 'Chromatic Approach Notes — Add chromatic leading tones and passing tones',
  6: 'Arpeggio Fills — Break long notes into chord figures',
  7: 'Cathedral Reverb — Spacious ecclesiastical reverb (70% wet, 2.5s decay)',
  8: 'Vibrato Wobble — Sine LFO modulation + tremolo wobble effect',
  9: 'Echo Cascade — Triplet-rhythm delays (375/750/1125ms) with feedback',
  10: 'Spacious Chorus — Combined reverb + vibrato + delay for ambient effect',
}

export default function EmblemPage({ params }: { params: { id: string } }) {
  const emblemId = parseInt(params.id)
  const emblem = emblems.emblems.find(e => e.id === emblemId)
  const phaseInfo = emblems.phases[emblem?.phase as keyof typeof emblems.phases]

  const prevId = emblemId > 1 ? emblemId - 1 : 50
  const nextId = emblemId < 50 ? emblemId + 1 : 1

  const [playingVariation, setPlayingVariation] = useState<number | null>(null)

  if (!emblem) {
    return (
      <main className="flex-1 container py-20">
        <p className="text-center text-slate-400">Emblem not found</p>
      </main>
    )
  }

  return (
    <main className="flex-1">
      {/* Navigation Header */}
      <header className="border-b border-slate-700 bg-slate-950/80 backdrop-blur-md sticky top-0 z-40">
        <nav className="container py-4 flex items-center justify-between">
          <Link href="/" className="text-xl font-bold gradient-text">
            FUGUEJUKEBOX
          </Link>
          <Link href="/#emblems" className="btn-secondary" style={{ padding: '0.5rem 1rem', fontSize: '0.9rem' }}>
            ← Back to Index
          </Link>
        </nav>
      </header>

      {/* Emblem Navigation */}
      <div className="border-b border-slate-700 bg-slate-900/50">
        <div className="container py-4 flex items-center justify-between">
          <Link href={`/emblem/${prevId}`} className="btn-secondary text-sm flex items-center gap-2">
            <ChevronLeft className="w-4 h-4" />
            Emblem {prevId}
          </Link>
          <p className="text-sm text-slate-400">
            {emblemId} / 50
          </p>
          <Link href={`/emblem/${nextId}`} className="btn-secondary text-sm flex items-center gap-2">
            Emblem {nextId}
            <ChevronRight className="w-4 h-4" />
          </Link>
        </div>
      </div>

      {/* Main Content */}
      <div className="container py-16">
        <div className="max-w-4xl">
          {/* Emblem Title Section */}
          <div className="mb-12">
            <div className="flex items-baseline gap-4 mb-4">
              <div className="text-6xl font-bold text-amber-600">{emblem.roman}</div>
              <div>
                <h1 className="mb-2">{emblem.title}</h1>
                <div className="flex gap-4 items-center">
                  <span className="text-sm px-3 py-1 bg-slate-800 rounded">{phaseInfo.name}</span>
                  <span className="text-sm text-slate-400">Emblem {emblem.id}/50</span>
                </div>
              </div>
            </div>

            <div className="divider"></div>
          </div>

          {/* Emblem Text */}
          <section className="mb-16 bg-slate-900/50 border border-slate-700 rounded-lg p-8">
            <h2 className="text-xl font-bold mb-4 text-amber-500">The Emblem</h2>

            <div className="space-y-6">
              <div>
                <h3 className="text-sm font-mono text-slate-400 mb-2">EPIGRAM</h3>
                <p className="text-lg italic">"{emblem.epigram}"</p>
              </div>

              <div>
                <h3 className="text-sm font-mono text-slate-400 mb-2">POEM</h3>
                <p className="text-lg italic whitespace-pre-line">{emblem.poem}</p>
              </div>

              <div>
                <h3 className="text-sm font-mono text-slate-400 mb-2">ALCHEMICAL PHASE</h3>
                <p>{phaseInfo.description}</p>
              </div>
            </div>
          </section>

          {/* Variations Section */}
          <section className="mb-16">
            <h2 className="text-2xl font-bold mb-8 flex items-center gap-3">
              <Volume2 className="w-6 h-6 text-amber-500" />
              10 Musical Variations
            </h2>

            <p className="text-slate-400 mb-12">
              Each emblem is transformed into 10 variations: 3 harmonic elaborations, 3 scalar improvisations,
              and 4 effect-based treatments. Play them in sequence to hear the melody evolve, or choose individual variations.
            </p>

            <div className="space-y-8">
              {/* Harmonic Variations */}
              <div>
                <h3 className="text-lg font-bold mb-4 text-slate-300">
                  ◆ Harmonic Elaborations (1-3)
                </h3>
                <div className="space-y-4 ml-4">
                  {[1, 2, 3].map((varNum) => (
                    <VariationCard
                      key={varNum}
                      emblemId={emblem.id}
                      variationNum={varNum}
                      description={VARIATION_DESCRIPTIONS[varNum as keyof typeof VARIATION_DESCRIPTIONS]}
                      isPlaying={playingVariation === varNum}
                      onPlay={() => setPlayingVariation(varNum)}
                    />
                  ))}
                </div>
              </div>

              {/* Scale Run Variations */}
              <div>
                <h3 className="text-lg font-bold mb-4 text-slate-300">
                  ◆ Scale Runs & Improvisations (4-6)
                </h3>
                <div className="space-y-4 ml-4">
                  {[4, 5, 6].map((varNum) => (
                    <VariationCard
                      key={varNum}
                      emblemId={emblem.id}
                      variationNum={varNum}
                      description={VARIATION_DESCRIPTIONS[varNum as keyof typeof VARIATION_DESCRIPTIONS]}
                      isPlaying={playingVariation === varNum}
                      onPlay={() => setPlayingVariation(varNum)}
                    />
                  ))}
                </div>
              </div>

              {/* Effect Variations */}
              <div>
                <h3 className="text-lg font-bold mb-4 text-slate-300">
                  ◆ Effect Treatments (7-10)
                </h3>
                <div className="space-y-4 ml-4">
                  {[7, 8, 9, 10].map((varNum) => (
                    <VariationCard
                      key={varNum}
                      emblemId={emblem.id}
                      variationNum={varNum}
                      description={VARIATION_DESCRIPTIONS[varNum as keyof typeof VARIATION_DESCRIPTIONS]}
                      isPlaying={playingVariation === varNum}
                      onPlay={() => setPlayingVariation(varNum)}
                    />
                  ))}
                </div>
              </div>
            </div>
          </section>

          {/* About This Variation */}
          <section className="bg-slate-900/50 border border-slate-700 rounded-lg p-8 mb-12">
            <h3 className="font-bold mb-4">About the Variations</h3>
            <p className="text-sm text-slate-400">
              Each variation is synthesized using square-wave NES-style synthesis (44.1 kHz, 16-bit PCM).
              The harmonic elaborations reharmonize the original melody. Scale runs add improvisation.
              Effects process the audio for ambient or experimental listening.
            </p>
          </section>

          {/* Navigation Footer */}
          <div className="border-t border-slate-700 pt-12 flex justify-between">
            <Link href={`/emblem/${prevId}`} className="btn-secondary flex items-center gap-2">
              <ChevronLeft className="w-4 h-4" />
              Previous Emblem
            </Link>
            <Link href="/#emblems" className="btn-secondary">
              Back to Index
            </Link>
            <Link href={`/emblem/${nextId}`} className="btn-secondary flex items-center gap-2">
              Next Emblem
              <ChevronRight className="w-4 h-4" />
            </Link>
          </div>
        </div>
      </div>
    </main>
  )
}

function VariationCard({
  emblemId,
  variationNum,
  description,
  isPlaying,
  onPlay,
}: {
  emblemId: number
  variationNum: number
  description: string
  isPlaying: boolean
  onPlay: () => void
}) {
  const filename = `emblem_${String(emblemId).padStart(2, '0')}_variation_${String(variationNum).padStart(2, '0')}.mp3`
  const mp3Path = `../../../FUGUEJUKEBOX/emblems/emblem_${String(emblemId).padStart(2, '0')}/${filename}`

  const categoryColors: { [key: number]: string } = {
    1: 'text-blue-400',
    2: 'text-blue-400',
    3: 'text-blue-400',
    4: 'text-green-400',
    5: 'text-green-400',
    6: 'text-green-400',
    7: 'text-purple-400',
    8: 'text-purple-400',
    9: 'text-purple-400',
    10: 'text-purple-400',
  }

  return (
    <div className="bg-slate-800/50 border border-slate-700 rounded-lg p-6 hover:border-amber-600 transition">
      <div className="flex items-start justify-between mb-4">
        <div>
          <h4 className={`font-bold mb-1 ${categoryColors[variationNum]}`}>
            Variation {variationNum}
          </h4>
          <p className="text-sm text-slate-400">{description}</p>
        </div>
      </div>

      <audio
        controls
        className="w-full"
        onPlay={onPlay}
        onPause={() => onPlay()}
      >
        <source src={mp3Path} type="audio/mpeg" />
        Your browser does not support the audio element.
      </audio>

      <p className="text-xs text-slate-500 mt-2">~34 seconds • 293KB • 192 kbps MP3</p>
    </div>
  )
}
