from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pathlib import Path
import json

app = FastAPI(title="Chiikawa Game API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

DATA_PATH = Path(__file__).resolve().parent / "highscore.json"

class ScoreSubmission(BaseModel):
    player: str = "Chiikawa"
    score: int


def load_highscore() -> dict:
    if not DATA_PATH.exists():
        DATA_PATH.write_text(json.dumps({"score": 0, "player": "Chiikawa"}, indent=2), encoding="utf-8")
    try:
        return json.loads(DATA_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {"score": 0, "player": "Chiikawa"}


def save_highscore(data: dict) -> None:
    DATA_PATH.write_text(json.dumps(data, indent=2), encoding="utf-8")


@app.get("/api/highscore")
def get_highscore() -> dict:
    return load_highscore()


@app.post("/api/highscore")
def submit_highscore(payload: ScoreSubmission) -> dict:
    if payload.score < 0:
        raise HTTPException(status_code=400, detail="Score must not be negative")

    highscore = load_highscore()
    if payload.score > highscore.get("score", 0):
        highscore.update({"score": payload.score, "player": payload.player})
        save_highscore(highscore)
        return {"status": "new-highscore", "highscore": highscore}

    return {"status": "ok", "highscore": highscore}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
