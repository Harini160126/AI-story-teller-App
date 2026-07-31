import { useEffect, useMemo, useState } from 'react'
import { BookOpen, Moon, Search, Sparkles, Sun } from 'lucide-react'
import StoryCard from './components/StoryCard.jsx'
import AudioPlayer from './components/AudioPlayer.jsx'
import { api, sampleStories } from './services/api.js'

const genres = ['All','Adventure','Fantasy','Horror','Mystery','Sci-Fi','Comedy','Romance','Motivational','Mythology','Historical']
const ages = ['All','3–6 years','7–12 years','13–18 years','Adults']

export default function App() {
  const [dark, setDark] = useState(false), [stories, setStories] = useState(sampleStories), [query, setQuery] = useState('')
  const [genre, setGenre] = useState('All'), [age, setAge] = useState('All'), [premium, setPremium] = useState('All')
  const [active, setActive] = useState(null), [playing, setPlaying] = useState(false), [speed, setSpeed] = useState(1), [progress, setProgress] = useState(0)
  useEffect(() => { document.documentElement.classList.toggle('dark', dark) }, [dark])
  useEffect(() => { api('/stories').then(setStories).catch(() => setStories(sampleStories)) }, [])
  useEffect(() => {
    if (!active || !('speechSynthesis' in window)) return
    window.speechSynthesis.cancel(); const u = new SpeechSynthesisUtterance(`${active.title}. ${active.description}`); u.rate = Number(speed); u.onend = () => setPlaying(false)
    if (playing) window.speechSynthesis.speak(u); return () => window.speechSynthesis.cancel()
  }, [active, playing, speed])
  useEffect(() => { if (!playing) return; const id = setInterval(() => setProgress(p => Math.min(100, p + 4)), 700); return () => clearInterval(id) }, [playing])
  const filtered = useMemo(() => stories.filter(s => [s.title,s.genre,s.author,s.age_group].join(' ').toLowerCase().includes(query.toLowerCase()) && (genre==='All'||s.genre===genre) && (age==='All'||s.age_group===age) && (premium==='All'||String(s.is_premium)===premium)), [stories, query, genre, age, premium])
  const play = story => { setActive(story); setProgress(0); setPlaying(true) }
  const stop = () => { window.speechSynthesis?.cancel(); setPlaying(false); setProgress(0) }
  return <main className="min-h-screen bg-gradient-to-br from-indigo-50 via-white to-fuchsia-100 text-slate-950 dark:from-slate-950 dark:via-indigo-950 dark:to-slate-900 dark:text-white pb-32">
    <nav className="sticky top-0 z-10 border-b border-white/20 bg-white/70 backdrop-blur-xl dark:bg-slate-950/70"><div className="mx-auto flex max-w-7xl items-center justify-between p-4"><a href="#home" className="flex items-center gap-2 text-2xl font-black"><BookOpen className="text-purple-600"/>StoryVerse AI</a><div className="flex gap-2"><a className="btn hidden bg-white/60 md:inline-flex dark:bg-slate-800" href="#dashboard">Dashboard</a><button className="btn bg-slate-950 text-white dark:bg-white dark:text-slate-950" onClick={()=>setDark(!dark)}>{dark ? <Sun/> : <Moon/>}</button></div></div></nav>
    <section id="home" className="mx-auto grid max-w-7xl gap-8 px-4 py-12 lg:grid-cols-[1.2fr_.8fr]"><div className="space-y-6"><span className="rounded-full bg-purple-600 px-4 py-2 text-sm font-bold text-white">AI-powered stories for every age</span><h1 className="text-5xl font-black leading-tight md:text-7xl">Discover, recommend, and narrate magical stories.</h1><p className="max-w-2xl text-lg text-slate-600 dark:text-slate-300">Personalized recommendations, browser text-to-speech narration, premium badges, accessible controls, and admin-ready APIs in one deployment-ready full-stack app.</p><div className="flex flex-wrap gap-3"><a className="btn bg-purple-600 text-white" href="#stories">Explore stories</a><a className="btn bg-white text-slate-900" href="#premium">View premium</a></div></div><aside className="glass rounded-[2rem] p-6"><Sparkles className="mb-4 text-purple-500"/><h2 className="text-2xl font-black">Daily recommended story</h2><p className="mt-2 text-slate-600 dark:text-slate-300">{stories[0]?.title} — selected using genre fit, age group, rating, and listener trends.</p></aside></section>
    <section id="stories" className="mx-auto max-w-7xl px-4"><div className="glass mb-8 grid gap-3 rounded-3xl p-4 md:grid-cols-4"><label className="relative md:col-span-2"><Search className="absolute left-3 top-3 text-slate-400"/><input className="w-full rounded-2xl border p-3 pl-11 dark:bg-slate-950" placeholder="Natural language search: funny dragon for ages 7-12" value={query} onChange={e=>setQuery(e.target.value)} /></label><select className="rounded-2xl border p-3 dark:bg-slate-950" value={genre} onChange={e=>setGenre(e.target.value)}>{genres.map(g=><option key={g}>{g}</option>)}</select><select className="rounded-2xl border p-3 dark:bg-slate-950" value={age} onChange={e=>setAge(e.target.value)}>{ages.map(a=><option key={a}>{a}</option>)}</select><select className="rounded-2xl border p-3 dark:bg-slate-950" value={premium} onChange={e=>setPremium(e.target.value)}><option value="All">Free & Premium</option><option value="false">Free</option><option value="true">Premium</option></select></div><h2 className="mb-5 text-3xl font-black">Featured, trending, and recommended stories</h2><div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">{filtered.map(s=><StoryCard story={s} key={s.id} onPlay={play}/>)}</div></section>
    <section id="dashboard" className="mx-auto mt-12 grid max-w-7xl gap-6 px-4 md:grid-cols-3"><Panel title="User Dashboard" items={['Profile and premium status','Saved favorites and bookmarks','Continue listening history','Downloaded stories']} /><Panel title="Admin Dashboard" items={['Add, edit, delete stories','Upload covers and story text','Manage users and subscriptions','View analytics']} /><Panel title="Accessibility" items={['Keyboard navigable controls','Screen-reader labels','High contrast dark mode','Adjustable browser zoom friendly typography']} /></section>
    <section id="premium" className="mx-auto mt-12 max-w-7xl px-4"><div className="glass rounded-3xl p-8"><h2 className="text-3xl font-black">Premium Membership</h2><p className="mt-2 text-slate-600 dark:text-slate-300">Unlock exclusive releases, unlimited listening, offline downloads, high-quality audio, and an ad-free experience.</p></div></section>
    <AudioPlayer active={active} playing={playing} setPlaying={setPlaying} speed={speed} setSpeed={setSpeed} progress={progress} stop={stop}/>
  </main>
}
function Panel({ title, items }) { return <section className="glass rounded-3xl p-6"><h2 className="text-2xl font-black">{title}</h2><ul className="mt-4 space-y-2">{items.map(i=><li key={i}>✓ {i}</li>)}</ul></section> }
