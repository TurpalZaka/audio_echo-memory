import game
from game import play_loop
from tutorial import run_tutorial
from speech import speak
from speech import set_rate

# Default settings
PROFILE = 1      # 1..4
NUM_KEYS = 4     # 4..6
TTS_RATE = 130   # 80..220


def get_key_blocking(num_keys: int):
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
    print("[q] Quit")
    return input("> ").strip()


def select_profile():
    global PROFILE
    p = input("Choose profile (1-4): ").strip()
    if p in ("1", "2", "3", "4"):
        PROFILE = int(p)
        speak(f"Profile {p} selected.")
    else:
        speak("Invalid profile. Please choose 1 to 4.")


def settings_menu():
    global NUM_KEYS, TTS_RATE

    while True:
        print("\nSettings")
        print(f"[1] TTS speed (current: {TTS_RATE})")
        print(f"[2] Difficulty / number of sounds (current: {NUM_KEYS})")
        print("[b] Back")
        c = input("> ").strip().lower()

        if c == "1":
            r = input("Set TTS rate (80-220): ").strip()
            if r.isdigit():
                TTS_RATE = max(80, min(220, int(r)))
                if set_rate is not None:
                    set_rate(TTS_RATE)
                speak(f"TTS speed set to {TTS_RATE}.")
            else:
                speak("Invalid rate. Please enter a number between 80 and 220.")

        elif c == "2":
            nk = input("Number of sounds (4-6): ").strip()
            if nk.isdigit():
                NUM_KEYS = max(4, min(6, int(nk)))
                speak(f"Difficulty set. Using {NUM_KEYS} sounds.")
            else:
                speak("Invalid number. Please enter 4, 5, or 6.")

        elif c == "b":
            return
        else:
            speak("Invalid choice.")


if __name__ == "__main__":
    # Apply default TTS rate if available
    if set_rate is not None:
        set_rate(TTS_RATE)

    # Speak menu instructions once at start
    speak(
        "Welcome to Audio Echo Memory. "
        "Press 1 for tutorial, 2 to play, 3 to select profile, 4 for settings, or Q to quit."
    )

    while True:
        choice = menu()

        if choice == "1":
            run_tutorial(lambda: get_key_blocking(NUM_KEYS))

        elif choice == "2":
            # Configure game with selected profile & difficulty
            game.configure(PROFILE, NUM_KEYS)

            score, high = play_loop(lambda: get_key_blocking(NUM_KEYS))
            print(f"Game over. Score={score}, HighScore={high}")
            speak(f"Game over. Your score was {score}. Your high score is {high}.")

        elif choice == "3":
            select_profile()

        elif choice == "4":
            settings_menu()

        elif choice.lower() == "q":
            break

        else:
            speak("Invalid choice. Press 1 for tutorial, 2 to play, 3 for profile, 4 for settings, or Q to quit.")
