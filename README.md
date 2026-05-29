# Chiikawa Clicker ✨

A tiny full-stack Chiikawa game with a cute Vue frontend and FastAPI backend. Tap the Chiikawa characters, chase the high score, and enjoy the pink bubble magic! .☘︎ ݁˖

## 🌸 Game Overview

Tap moving Chiikawa characters as fast as you can in 20 seconds. Every hit earns points, and the backend keeps the high score safe in a JSON file.

### Features

- Vue 3 frontend with a playful clicker UI
- FastAPI backend with a simple high score API
- High score saved in `backend/highscore.json`
- Frontend proxies `/api` requests to the backend for easy local play
- Floating bubble animation and cute heart cursor

## 🚀 Quick Start

### 1) Start the backend

Open a terminal and run:

```bash
cd backend
./venv/Scripts/python main.py
```

Then visit `http://127.0.0.1:8000` if you want to verify the server is running.

### 2) Start the frontend

Open another terminal and run:

```bash
cd frontend
npm install
npm run dev
```

Open the Vite URL shown in the terminal (usually `http://127.0.0.1:5173`).

> If you are on Windows and using Git Bash, the backend command is still `./venv/Scripts/python main.py`.

## 🧩 Backend API

- `GET /api/highscore` — returns the current high score
- `POST /api/highscore` — submit a new score like this:

```json
{
  "player": "You",
  "score": 120
}
```

## 📁 Project structure

- `frontend/` — Vue app and game UI
- `backend/` — FastAPI server and local high score storage
- `README.md` — this cute setup guide

## 💡 Notes

- Start the backend first so the frontend can load and submit scores.
- High scores are stored in `backend/highscore.json` and persist across runs.
- Want to change the game? Add more Chiikawa images in `frontend/src/assets/`.

## 💖 Play locally

1. Run the backend
2. Run the frontend
3. Click the Chiikawa bubbles and try to beat the high score
4. Enjoy the cute animation and pink vibes!

Have fun! ݁˖✧