from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import admin, ai, audio, auth, premium, stories
from app.core.config import settings
from app.core.database import Base, engine

Base.metadata.create_all(bind=engine)
app = FastAPI(title="StoryVerse AI API", version="1.0.0", description="AI-powered story recommendation and narration platform")
app.add_middleware(CORSMiddleware, allow_origins=[o.strip() for o in settings.cors_origins.split(",")], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
for router in [auth.router, stories.router, ai.router, audio.router, premium.router, admin.router]:
    app.include_router(router, prefix="/api")

@app.get("/health")
def health():
    return {"status": "ok", "app": settings.app_name}
