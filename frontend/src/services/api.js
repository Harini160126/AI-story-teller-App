const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api'
export async function api(path, options = {}) {
  const token = localStorage.getItem('storyverse_token')
  const headers = { 'Content-Type': 'application/json', ...(token ? { Authorization: `Bearer ${token}` } : {}), ...options.headers }
  const res = await fetch(`${API_URL}${path}`, { ...options, headers })
  if (!res.ok) throw new Error((await res.json()).detail || 'Request failed')
  return res.json()
}
export const sampleStories = [
  { id: 1, title: 'Moonlit Mango Tree', genre: 'Fantasy', age_group: '3–6 years', author: 'StoryVerse Studio', rating: 4.8, listeners: 2310, reading_time: 8, is_premium: false, cover_image: 'https://picsum.photos/seed/moonlit/640/420', description: 'A gentle bedtime journey under a glowing mango tree.' },
  { id: 2, title: 'Clockwork Dragon', genre: 'Adventure', age_group: '7–12 years', author: 'StoryVerse Studio', rating: 4.7, listeners: 4080, reading_time: 12, is_premium: true, cover_image: 'https://picsum.photos/seed/dragon/640/420', description: 'A young inventor repairs a dragon before sunrise.' },
  { id: 3, title: 'Stardust Express', genre: 'Sci-Fi', age_group: '13–18 years', author: 'StoryVerse Studio', rating: 4.6, listeners: 3590, reading_time: 15, is_premium: false, cover_image: 'https://picsum.photos/seed/stardust/640/420', description: 'Friends board a train that maps forgotten constellations.' }
]
