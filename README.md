# StoryVerse AI

StoryVerse AI is a full-stack AI-powered story recommendation and narration web application for children, teens, and adults. It includes a modern React UI, FastAPI backend, JWT authentication, SQLAlchemy models, PostgreSQL-ready configuration, Swagger/OpenAPI docs, premium membership flows, admin analytics, and sample data.

## Features

- JWT registration, login, password hashing, and profile endpoint.
- Home sections for featured, trending, new releases, popular genres, and daily recommendations.
- Story discovery by title, genre, author, age group, premium/free status, and rating.
- AI-style endpoints for personalized recommendations, summaries, similar stories, natural language search support, and prompt-generated story drafts.
- Browser speech-synthesis narration with play, pause, stop, speed control, progress, and accessible labels.
- Premium plans, subscriptions, payments, favorites, listening history, continue-listening progress, and admin analytics.
- Responsive glassmorphism UI with dark/light mode, keyboard-friendly controls, and high-contrast-friendly design.

## Project Structure

```text
backend/app/api        FastAPI routers for auth, stories, AI, audio, premium, admin
backend/app/core       Settings, database session, JWT/password security
backend/app/models     SQLAlchemy ORM tables
backend/app/schemas    Pydantic request/response schemas
frontend/src/components Reusable React components
frontend/src/services  API client and fallback sample data
docs/schema.sql        PostgreSQL database schema
```

## Backend Setup

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python -m app.seed
uvicorn app.main:app --reload
```

API docs are available at `http://localhost:8000/docs` and OpenAPI JSON at `http://localhost:8000/openapi.json`.

Demo admin credentials after seeding:

- Email: `admin@storyverse.ai`
- Password: `admin123`

## Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Open `http://localhost:5173`.

## PostgreSQL / Docker

```bash
docker compose up --build
```

The default compose file starts PostgreSQL, FastAPI, and the production frontend container.

## Database Schema

See `docs/schema.sql` for the normalized tables: Users, Stories, Genres, AgeGroups, Favorites, ListeningHistory, PremiumSubscriptions, Payments, and Recommendations.

## Deployment Notes

- Change `SECRET_KEY` before production.
- Set `DATABASE_URL` to a managed PostgreSQL connection string.
- Restrict `CORS_ORIGINS` to deployed frontend domains.
- Replace the demo AI and audio responses with provider-backed LLM and TTS integrations when credentials are available.
