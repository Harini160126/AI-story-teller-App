from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_current_user, require_admin
from app.core.database import get_db
from app.models.models import Payment, PremiumSubscription, User

router = APIRouter(prefix="/premium", tags=["Premium"])

@router.get("/plans")
def plans():
    return {"free": ["Curated free stories", "Limited listening"], "premium": ["Exclusive stories", "Unlimited listening", "Offline downloads", "High-quality audio", "Ad-free experience"]}

@router.post("/subscribe")
def subscribe(user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    sub = PremiumSubscription(user_id=user.id, plan="premium", active=True)
    db.add(sub); db.add(Payment(user_id=user.id, amount=9.99, status="demo-approved")); db.commit()
    return {"active": True, "plan": "premium"}

@router.get("/admin/subscriptions", dependencies=[Depends(require_admin)])
def subscriptions(db: Session = Depends(get_db)):
    return db.query(PremiumSubscription).all()
