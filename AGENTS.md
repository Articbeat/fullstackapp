# AGENTS.md

## Project overview

This repo contains a small full-stack app:

- Backend: Flask REST API using SQLAlchemy and Flask-CORS
- Frontend: React app bootstrapped with Vite
- Shared data model: contact records with first name, last name, and email

## Important paths

- Backend entry points: [backend/main.py](backend/main.py), [backend/config.py](backend/config.py), [backend/models.py](backend/models.py)
- Frontend app: [frontend/src/App.jsx](frontend/src/App.jsx)
- Frontend config: [frontend/package.json](frontend/package.json), [frontend/vite.config.js](frontend/vite.config.js)
- Project docs: [frontend/README.md](frontend/README.md)

## Working conventions

- Keep backend and frontend concerns separate. API logic belongs in the backend folder; UI logic belongs in the frontend folder.
- Prefer small, clear changes. This project is intentionally simple; avoid adding heavy abstractions or unnecessary frameworks.
- Maintain compatibility with the current stack: Flask, SQLAlchemy, Flask-CORS, React, and Vite.
- Preserve CORS and database configuration when changing backend startup or API routes.

## Backend guidance

- The Flask app is configured in [backend/config.py](backend/config.py).
- Database models are defined in [backend/models.py](backend/models.py).
- API routes and app startup logic should live in [backend/main.py](backend/main.py).
- Use Flask JSON responses with `jsonify(...)` for API output.
- If you add endpoints, keep them consistent with the existing contact resource model.
- Run the backend from the backend directory with:

  ```bash
  python main.py
  ```

- The app is expected to run with a local SQLite database file in the backend directory.

## Frontend guidance

- The frontend is a Vite React app under [frontend](frontend).
- Use the scripts in [frontend/package.json](frontend/package.json):

  ```bash
  cd frontend
  npm install
  npm run dev
  ```

- For production builds, use:

  ```bash
  cd frontend
  npm run build
  ```

- Keep React component changes local to the frontend app; avoid adding backend logic into UI files.
- If the frontend calls the API, use the Flask backend URL (typically `http://localhost:5000`) unless the project config says otherwise.

## Validation

- For backend changes, run the Flask app and verify the expected HTTP behavior manually.
- For frontend changes, run Vite locally and confirm the app renders without console errors.
- If you change shared data contracts, update both sides of the stack together.
- There are no dedicated automated tests in this repo yet, so verify with the smallest realistic local run.

## Common pitfalls

- Do not break the SQLAlchemy model structure or the database URI in [backend/config.py](backend/config.py).
- Do not introduce frontend dependencies without updating the project config.
- Be careful with naming consistency: the contact model uses `first_name`, `last_name`, and `email` on the backend, and the frontend may map these to camelCase fields.
- Keep CORS enabled so the React frontend can access the Flask API during local development.
