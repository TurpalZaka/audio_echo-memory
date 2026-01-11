import json
import os

SETTINGS_FILE = "settings.json"
DEFAULT_RATE = 130

def load_tts_rate() -> int:
    """Load TTS rate from settings.json. Returns DEFAULT_RATE if missing/invalid."""
    if not os.path.exists(SETTINGS_FILE):
        return DEFAULT_RATE

    try:
        with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        rate = int(data.get("tts_rate", DEFAULT_RATE))
        return max(80, min(220, rate))
    except Exception:
        return DEFAULT_RATE

def save_tts_rate(rate: int) -> None:
    """Save TTS rate to settings.json."""
    rate = max(80, min(220, int(rate)))
    data = {"tts_rate": rate}
    with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
