from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.models import Story

router = APIRouter(prefix="/audio", tags=["Audio"])

@router.get("/{story_id}")
def audio_metadata(story_id: int, db: Session = Depends(get_db)):
    story = db.get(Story, story_id)
    return {"story_id": story_id, "narration_text": story.text, "download_allowed": not story.is_premium, "voice": "browser-speech-synthesis"}
