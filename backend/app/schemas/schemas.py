from pydantic import BaseModel, EmailStr

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class UserCreate(BaseModel):
    email: EmailStr
    full_name: str
    password: str
    favorite_genres: str = "Fantasy,Adventure"

class UserRead(BaseModel):
    id: int
    email: EmailStr
    full_name: str
    is_admin: bool
    favorite_genres: str
    model_config = {"from_attributes": True}

class StoryBase(BaseModel):
    title: str
    cover_image: str
    description: str
    text: str
    author: str
    reading_time: int
    rating: float = 4.5
    listeners: int = 0
    is_premium: bool = False
    genre_id: int
    age_group_id: int

class StoryCreate(StoryBase):
    pass

class StoryRead(StoryBase):
    id: int
    genre: str
    age_group: str

class HistoryUpdate(BaseModel):
    story_id: int
    progress_seconds: int
    completed: bool = False
