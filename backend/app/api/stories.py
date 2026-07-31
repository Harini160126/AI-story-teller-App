from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import or_
from sqlalchemy.orm import Session
from app.api.deps import get_current_user, require_admin
from app.core.database import get_db
from app.models.models import AgeGroup, Favorite, Genre, ListeningHistory, Story, User
from app.schemas.schemas import HistoryUpdate, StoryCreate

router = APIRouter(prefix="/stories", tags=["Stories"])

def serialize(story: Story):
    return {**story.__dict__, "genre": story.genre.name, "age_group": story.age_group.label}

@router.get("")
def list_stories(q: str | None = None, genre: str | None = None, age_group: str | None = None, premium: bool | None = None, min_rating: float = 0, db: Session = Depends(get_db)):
    query = db.query(Story).join(Genre).join(AgeGroup).filter(Story.rating >= min_rating)
    if q:
        like = f"%{q}%"; query = query.filter(or_(Story.title.ilike(like), Story.author.ilike(like), Story.description.ilike(like), Genre.name.ilike(like)))
    if genre: query = query.filter(Genre.name == genre)
    if age_group: query = query.filter(AgeGroup.label == age_group)
    if premium is not None: query = query.filter(Story.is_premium == premium)
    return [serialize(s) for s in query.order_by(Story.rating.desc()).all()]

@router.get("/home")
def home(db: Session = Depends(get_db)):
    stories = db.query(Story).all()
    return {
        "featured": [serialize(s) for s in stories[:3]],
        "trending": [serialize(s) for s in sorted(stories, key=lambda x: x.listeners, reverse=True)[:6]],
        "new_releases": [serialize(s) for s in stories[-6:]],
        "popular_genres": [g.name for g in db.query(Genre).all()],
        "daily_recommended": serialize(stories[0]) if stories else None,
    }

@router.get("/{story_id}")
def detail(story_id: int, db: Session = Depends(get_db)):
    story = db.get(Story, story_id)
    if not story: raise HTTPException(status_code=404, detail="Story not found")
    return serialize(story)

@router.post("", dependencies=[Depends(require_admin)])
def create_story(payload: StoryCreate, db: Session = Depends(get_db)):
    story = Story(**payload.model_dump()); db.add(story); db.commit(); db.refresh(story); return serialize(story)

@router.put("/{story_id}", dependencies=[Depends(require_admin)])
def update_story(story_id: int, payload: StoryCreate, db: Session = Depends(get_db)):
    story = db.get(Story, story_id)
    if not story: raise HTTPException(status_code=404, detail="Story not found")
    for key, value in payload.model_dump().items(): setattr(story, key, value)
    db.commit(); db.refresh(story); return serialize(story)

@router.delete("/{story_id}", dependencies=[Depends(require_admin)])
def delete_story(story_id: int, db: Session = Depends(get_db)):
    story = db.get(Story, story_id)
    if not story: raise HTTPException(status_code=404, detail="Story not found")
    db.delete(story); db.commit(); return {"ok": True}

@router.post("/{story_id}/favorite")
def favorite(story_id: int, user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    if not db.query(Favorite).filter_by(user_id=user.id, story_id=story_id).first():
        db.add(Favorite(user_id=user.id, story_id=story_id)); db.commit()
    return {"saved": True}

@router.post("/history")
def history(payload: HistoryUpdate, user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    item = db.query(ListeningHistory).filter_by(user_id=user.id, story_id=payload.story_id).first() or ListeningHistory(user_id=user.id, story_id=payload.story_id)
    item.progress_seconds = payload.progress_seconds; item.completed = payload.completed
    db.add(item); db.commit(); return {"saved": True}
