from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "StoryVerse AI"
    database_url: str = "sqlite:///./storyverse.db"
    secret_key: str = "dev-secret-change-me"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60
    cors_origins: str = "http://localhost:5173"

    class Config:
        env_file = ".env"

settings = Settings()
