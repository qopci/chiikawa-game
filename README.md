# Chiikawa Clicker

A tiny full-stack Chiikawa-themed game built with Vue on the frontend and FastAPI on the backend.

## Game Overview

In this small game, the player taps moving Chiikawa characters as fast as possible within 20 seconds. Each hit increases the score, and the backend tracks the high score using a simple JSON persistence file.

### Features

- Vue 3 frontend with a simple clicker game UI
- FastAPI backend with a high score API
- Backend persistence in `backend/highscore.json`
- Frontend proxy configured for `/api` requests to the backend

## Run the app

### Backend

Open a terminal and run:

```bash
cd /c/Users/seonp/sdev378/chiikawa-game/backend
./venv/Scripts/python main.py
```

> If you are using PowerShell or CMD, use:
>
```powershell
cd C:\Users\seonp\sdev378\chiikawa-game\backend
venv\Scripts\python main.py
```

The backend will start on `http://127.0.0.1:8000`.

### Frontend

In a second terminal, run:

```bash
cd /c/Users/seonp/sdev378/chiikawa-game/frontend
npm run dev
```

Then open the Vite URL shown in the terminal (usually `http://127.0.0.1:5173`).

## Backend API

- `GET /api/highscore` — returns the current high score
- `POST /api/highscore` — submit a new score payload:

```json
{
  "player": "You",
  "score": 120
}
```

## Project structure

- `frontend/` — Vue application
- `backend/` — FastAPI backend and virtual environment
- `.gitignore` — ignores node_modules, venv, and other generated files

## Notes

- Make sure the backend is running before starting the frontend so the game can load the high score and submit new scores.
- The high score persists across runs in `backend/highscore.json`.
