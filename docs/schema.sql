CREATE TABLE users (id SERIAL PRIMARY KEY, email VARCHAR(255) UNIQUE NOT NULL, full_name VARCHAR(120) NOT NULL, hashed_password VARCHAR(255) NOT NULL, is_admin BOOLEAN DEFAULT FALSE, favorite_genres VARCHAR(255), created_at TIMESTAMP DEFAULT now());
CREATE TABLE genres (id SERIAL PRIMARY KEY, name VARCHAR(80) UNIQUE NOT NULL);
CREATE TABLE age_groups (id SERIAL PRIMARY KEY, label VARCHAR(40) UNIQUE NOT NULL);
CREATE TABLE stories (id SERIAL PRIMARY KEY, title VARCHAR(180) NOT NULL, cover_image VARCHAR(500), description TEXT, text TEXT, author VARCHAR(120), reading_time INTEGER, rating FLOAT, listeners INTEGER, is_premium BOOLEAN, genre_id INTEGER REFERENCES genres(id), age_group_id INTEGER REFERENCES age_groups(id));
CREATE TABLE favorites (id SERIAL PRIMARY KEY, user_id INTEGER REFERENCES users(id), story_id INTEGER REFERENCES stories(id));
CREATE TABLE listening_history (id SERIAL PRIMARY KEY, user_id INTEGER REFERENCES users(id), story_id INTEGER REFERENCES stories(id), progress_seconds INTEGER DEFAULT 0, completed BOOLEAN DEFAULT FALSE, updated_at TIMESTAMP DEFAULT now());
CREATE TABLE premium_subscriptions (id SERIAL PRIMARY KEY, user_id INTEGER REFERENCES users(id), plan VARCHAR(40), active BOOLEAN DEFAULT FALSE);
CREATE TABLE payments (id SERIAL PRIMARY KEY, user_id INTEGER REFERENCES users(id), amount FLOAT, status VARCHAR(40));
CREATE TABLE recommendations (id SERIAL PRIMARY KEY, user_id INTEGER REFERENCES users(id), story_id INTEGER REFERENCES stories(id), reason VARCHAR(255));
