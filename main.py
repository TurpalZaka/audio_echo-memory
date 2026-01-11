import game
from game import play_loop
from tutorial import run_tutorial
from speech import speak, set_rate
from settings import load_tts_rate, save_tts_rate

# Runtime choices (only TTS rate is persisted)
PROFILE = 1      # 1..4 (not persisted)
NUM_KEYS = 4     # 4..6 (not persisted)
TTS_RATE = load_tts_rate()  # persisted

# Apply TTS rate immediately on startup
set_rate(TTS_RATE)


def speak_main_menu():
    speak(
        "Press 1 for tutorial. "
        "Press 2 to play. "
        "Press 3 to select profile. "
        "Press 4 for settings. "
        "Press Q to quit. "
        "Press H to repeat these options."
    )


def speak_settings_menu():
    speak(
        f"Settings menu. Current TTS speed is {TTS_RATE}. "
        f"Current difficulty is {NUM_KEYS} sounds. "
        "Press 1 to change TTS speed. "
        "Press 2 to change difficulty. "
        "Press B to go back. "
        "Press H to repeat these options."
    )


def get_key_blocking(num_keys: int):
    """Ask for a key 1..num_keys, with spoken error messages."""
    allowed = [str(i) for i in range(1, num_keys + 1)]
    allowed_str = ", ".join(allowed)

    while True:
        k = input(f"Press key (1-{num_keys}): ").strip()
        if not k:
            speak(f"Please press one of the keys {allowed_str}.")
            continue

        key = k[0]
        if key not in allowed:
            speak(f"Invalid key. Use keys {allowed_str}.")
            continue

        return key


def menu():
    print("\nAudio Echo Memory")
    print("[1] Tutorial")
    print("[2] Play")
    print("[3] Select Profile (1-4)")
    print("[4] Settings (TTS speed / Difficulty)")
    print("[h] Help (repeat options)")
    print("[q] Quit")
    return input("> ").strip().lower()


def select_profile():
    global PROFILE
    speak(
        f"Current profile is {PROFILE}. "
        "Choose profile 1-4."
    )

    p = input("Choose profile (1-4): ").strip()
    if p in ("1", "2", "3", "4"):
        PROFILE = int(p)
        speak(f"Profile {p} selected.")
    else:
        speak("Invalid profile. Please choose 1 to 4.")


def settings_menu():
    global NUM_KEYS, TTS_RATE

    speak_settings_menu()

    while True:
        print("\nSettings")
        print(f"[1] TTS speed (current: {TTS_RATE})")
        print(f"[2] Difficulty / number of sounds (current: {NUM_KEYS})")
        print("[h] Help (repeat options)")
        print("[b] Back")
        c = input("> ").strip().lower()

        if c == "h":
            speak_settings_menu()
            continue

        if c == "1":
            speak("Set TTS rate (80-220)")
            r = input("Set TTS rate (80-220): ").strip()
            if r.isdigit():
                TTS_RATE = max(80, min(220, int(r)))
                set_rate(TTS_RATE)
                save_tts_rate(TTS_RATE)  # persist only rate
                speak(f"TTS speed set to {TTS_RATE}.")
                speak_settings_menu()
            else:
                speak("Invalid rate. Please enter a number between 80 and 220.")
                speak_settings_menu()

        elif c == "2":
            speak("Set number of sounds (4-6)")
            nk = input("Number of sounds (4-6): ").strip()
            if nk.isdigit():
                NUM_KEYS = max(4, min(6, int(nk)))
                speak(f"Difficulty set. Using {NUM_KEYS} sounds.")
                speak_settings_menu()
            else:
                speak("Invalid number. Please enter 4, 5, or 6.")
                speak_settings_menu()

        elif c == "b":
            speak_main_menu()  # peak again when returning
            return

        else:
            speak("Invalid choice.")
            speak_settings_menu()


if __name__ == "__main__":
    # Speak main menu at start
    speak(
        "Welcome to Audio Echo Memory."
    )
    speak_main_menu()

    while True:
        choice = menu()

        if choice == "h":
            speak_main_menu()
            continue

        if choice == "1":
            # Tutorial adapts automatically because input range is NUM_KEYS
            run_tutorial(lambda: get_key_blocking(NUM_KEYS), num_keys=NUM_KEYS)
            speak_main_menu()  # speak again after returning

        elif choice == "2":
            # Configure game with selected profile & difficulty
            game.configure(PROFILE, NUM_KEYS)
            score, high = play_loop(lambda: get_key_blocking(NUM_KEYS))
            print(f"Game over. Score={score}, HighScore={high}")
            speak(f"Game over. Your score was {score}. Your high score is {high}.")
            speak_main_menu()  # speak again after returning

        elif choice == "3":
            select_profile()
            speak_main_menu()  # speak again after returning

        elif choice == "4":
            settings_menu()

        elif choice == "q":
            break

        else:
            speak("Invalid choice.")
            speak_main_menu()
