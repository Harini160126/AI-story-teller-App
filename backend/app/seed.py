from app.core.database import Base, SessionLocal, engine
from app.core.security import hash_password
from app.models.models import AgeGroup, Genre, Story, User

GENRES = ["Adventure", "Fantasy", "Horror", "Mystery", "Sci-Fi", "Comedy", "Romance", "Motivational", "Mythology", "Historical"]
AGES = ["3–6 years", "7–12 years", "13–18 years", "Adults"]

def seed():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    if not db.query(Genre).first():
        genres = [Genre(name=g) for g in GENRES]; ages = [AgeGroup(label=a) for a in AGES]
        db.add_all(genres + ages); db.commit()
        for i, title in enumerate(["Moonlit Mango Tree", "Clockwork Dragon", "The Library of Clouds", "Laughing Lighthouse", "Stardust Express", "The Brave Little Lantern", "Mystery at Maple Lane", "Echoes of Olympus"]):
            db.add(Story(title=title, cover_image=f"https://picsum.photos/seed/storyverse{i}/640/420", description=f"A vivid StoryVerse adventure called {title}.", text=f"Welcome to {title}. This narrated sample is calm, descriptive, and accessible for every listener.", author="StoryVerse Studio", reading_time=6+i, rating=4.2+(i%5)/10, listeners=800+i*221, is_premium=i%3==0, genre_id=(i%len(GENRES))+1, age_group_id=(i%len(AGES))+1))
        db.add(User(email="admin@storyverse.ai", full_name="Admin User", hashed_password=hash_password("admin123"), is_admin=True, favorite_genres="Fantasy,Sci-Fi"))
        db.commit()
    db.close()

if __name__ == "__main__":
    seed()
