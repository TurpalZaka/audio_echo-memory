import pyttsx3

def speak(text: str):
    print("[TTS]:", text, flush=True)
    engine = pyttsx3.init()
    engine.setProperty("rate", 130)
    engine.setProperty("volume", 0.9)

    # Force English Zira voice
    engine.setProperty(
        "voice",
        "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0"
    )

    engine.say(text)
    engine.runAndWait()
    engine.stop()
