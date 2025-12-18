import json
import os

PATH = "highscores.json"

def _default():
    return {"1": 0, "2": 0, "3": 0, "4": 0}

def _load_all():
    if not os.path.exists(PATH):
        data = _default()
        _save_all(data)
        return data
    try:
        with open(PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception:
        data = _default()
    # ensure keys exist
    for k in ("1", "2", "3", "4"):
        if k not in data:
            data[k] = 0
    return data

def _save_all(data):
    with open(PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def load_highscore(profile: int) -> int:
    data = _load_all()
    return int(data.get(str(profile), 0))

def save_highscore(profile: int, score: int):
    data = _load_all()
    data[str(profile)] = int(score)
    _save_all(data)
