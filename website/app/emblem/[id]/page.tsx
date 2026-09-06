import emblems from '@/data/emblems.json'
import EmblemView from './EmblemView'

// Server shell for the emblem route. The view itself is a client component
// (it holds playback state), and a client component cannot export
// generateStaticParams — which `output: 'export'` requires in order to know
// which /emblem/<id>/ pages to write out. So the shell enumerates the ids and
// hands each one to the view.
export function generateStaticParams() {
  return emblems.emblems.map((e) => ({ id: String(e.id) }))
}

export default function EmblemPage({ params }: { params: { id: string } }) {
  return <EmblemView id={params.id} />
}
