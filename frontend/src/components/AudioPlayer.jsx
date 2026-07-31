import { Pause, Play, Square } from 'lucide-react'
export default function AudioPlayer({ active, playing, setPlaying, speed, setSpeed, progress, stop }) {
  return <section className="fixed inset-x-4 bottom-4 z-20 mx-auto max-w-4xl glass rounded-3xl p-4" aria-live="polite">
    <div className="flex flex-col gap-3 md:flex-row md:items-center"><div className="flex-1"><p className="text-sm text-slate-500">Now narrating</p><strong>{active?.title || 'Choose a story'}</strong><div className="mt-2 h-2 rounded-full bg-slate-200"><div className="h-2 rounded-full bg-purple-600" style={{width:`${progress}%`}} /></div></div>
    <button className="btn bg-purple-600 text-white" onClick={() => setPlaying(!playing)} aria-label={playing ? 'Pause narration' : 'Play narration'}>{playing ? <Pause/> : <Play/>}</button>
    <button className="btn bg-slate-200 text-slate-900" onClick={stop} aria-label="Stop narration"><Square/></button>
    <label className="font-semibold">Speed <select value={speed} onChange={e=>setSpeed(e.target.value)} className="rounded-xl border p-2 dark:bg-slate-950" aria-label="Narration speed"><option>0.5</option><option>1</option><option>1.5</option><option>2</option></select>x</label></div>
  </section>
}
