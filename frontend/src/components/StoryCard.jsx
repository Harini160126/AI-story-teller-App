import { Headphones, Star } from 'lucide-react'
export default function StoryCard({ story, onPlay }) {
  return <article className="glass rounded-3xl overflow-hidden hover:-translate-y-1 transition" tabIndex="0" aria-label={`${story.title} story card`}>
    <img src={story.cover_image} alt="" className="h-44 w-full object-cover" />
    <div className="p-5 space-y-3"><div className="flex justify-between gap-3"><span className="rounded-full bg-purple-100 px-3 py-1 text-sm font-bold text-purple-700 dark:bg-purple-400/20 dark:text-purple-200">{story.genre}</span><span className="rounded-full bg-amber-100 px-3 py-1 text-sm font-bold text-amber-700">{story.is_premium ? 'Premium' : 'Free'}</span></div>
    <h3 className="text-xl font-black">{story.title}</h3><p className="text-sm text-slate-600 dark:text-slate-300">{story.description}</p>
    <div className="flex items-center justify-between text-sm"><span>{story.age_group}</span><span className="flex items-center gap-1"><Star size={16} className="fill-yellow-400 text-yellow-400" />{story.rating}</span><span className="flex items-center gap-1"><Headphones size={16}/>{story.listeners}</span></div>
    <button onClick={() => onPlay(story)} className="btn w-full bg-slate-950 text-white dark:bg-white dark:text-slate-950">Play narration</button></div>
  </article>
}
