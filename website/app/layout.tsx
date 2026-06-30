import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'FUGUEJUKEBOX',
  description: 'Atalanta Fugiens Chiptune Variations - 50 Emblems × 10 Musical Interpretations',
  viewport: 'width=device-width, initial-scale=1',
  charset: 'utf-8',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <head>
        <meta name="theme-color" content="#0f172a" />
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" />
        <link href="https://fonts.googleapis.com/css2?family=EB+Garamond:wght@400;500;700&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet" />
      </head>
      <body className="bg-slate-950 text-slate-100 font-serif antialiased">
        <div className="min-h-screen flex flex-col">
          {children}
        </div>
      </body>
    </html>
  )
}
