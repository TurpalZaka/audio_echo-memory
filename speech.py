import pyttsx3

# Default TTS settings
_TTS_RATE = 130
_TTS_VOLUME = 0.9


def set_rate(rate: int):
    global _TTS_RATE
    try:
        rate = int(rate)
    except Exception:
        return
    _TTS_RATE = max(80, min(220, rate))

def speak(text: str):
    print("[TTS]:", text, flush=True)
    engine = pyttsx3.init()


    # Apply properties
    engine.setProperty("rate", _TTS_RATE)
    engine.setProperty("volume", _TTS_VOLUME)

    # Force English Zira voice
    engine.setProperty(
        "voice",
        "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0"
    )

    engine.say(text)
    engine.runAndWait()
    engine.stop()
