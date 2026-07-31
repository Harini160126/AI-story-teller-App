from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import require_admin
from app.core.database import get_db
from app.models.models import Favorite, ListeningHistory, Payment, PremiumSubscription, Story, User

router = APIRouter(prefix="/admin", tags=["Admin"], dependencies=[Depends(require_admin)])

@router.get("/analytics")
def analytics(db: Session = Depends(get_db)):
    return {"users": db.query(User).count(), "stories": db.query(Story).count(), "favorites": db.query(Favorite).count(), "listening_sessions": db.query(ListeningHistory).count(), "payments": db.query(Payment).count(), "subscriptions": db.query(PremiumSubscription).count()}

@router.get("/users")
def users(db: Session = Depends(get_db)):
    return db.query(User).all()
