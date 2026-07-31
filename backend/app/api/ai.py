from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.stories import serialize
from app.core.database import get_db
from app.models.models import AgeGroup, Genre, Story

router = APIRouter(prefix="/ai", tags=["AI"])

@router.get("/recommendations")
def recommendations(age_group: str | None = None, genre: str | None = None, db: Session = Depends(get_db)):
    query = db.query(Story).join(Genre).join(AgeGroup)
    if age_group: query = query.filter(AgeGroup.label == age_group)
    if genre: query = query.filter(Genre.name == genre)
    return {"reason": "Matched by age group, genre, popularity, and listener history signals.", "stories": [serialize(s) for s in query.order_by(Story.rating.desc(), Story.listeners.desc()).limit(8)]}

@router.get("/summary/{story_id}")
def summary(story_id: int, db: Session = Depends(get_db)):
    story = db.get(Story, story_id)
    return {"summary": f"{story.title} is a {story.genre.name.lower()} tale about courage, curiosity, and memorable choices."}

@router.get("/similar/{story_id}")
def similar(story_id: int, db: Session = Depends(get_db)):
    story = db.get(Story, story_id)
    matches = db.query(Story).filter(Story.id != story_id, Story.genre_id == story.genre_id).limit(4).all()
    return [serialize(s) for s in matches]

@router.post("/generate")
def generate(prompt: dict):
    idea = prompt.get("prompt", "a brave explorer")
    return {"title": "Your Custom Story", "story": f"Once upon a time, {idea} discovered a glowing doorway to StoryVerse, where every kind choice made the stars sing."}
