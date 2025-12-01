from game import play_loop
from tutorial import run_tutorial
from speech import speak




def get_key_blocking():
    """Ask for a key 1-4, with spoken error messages."""
    while True:
        k = input("Press key (1-4): ").strip()
        if not k:
            speak("Please press one of the keys 1, 2, 3 or 4")
            continue

        key = k[0]
        if key not in ("1", "2", "3", "4"):
            speak("Invalid key. Use keys 1, 2, 3 or 4")
            continue

        return key


def menu():
    """Text menu (audio instructions are spoken once at program start)"""
    print("\nAudio Echo Memory")
    print("[1] Tutorial  [2] Play  [q] Quit")
    return input("> ").strip()


if __name__ == "__main__":
    # One single, long TTS sentence with all menu info
    speak(
        "Welcome to Audio Echo Memory. "
        "Press 1 for tutorial, "
        "press 2 to play, "
        "press Q to quit."
    )

    while True:
        choice = menu()

        if choice == "1":
            run_tutorial(get_key_blocking)

        elif choice == "2":
            score, high = play_loop(get_key_blocking)
            print(f"Game over. Score={score}, HighScore={high}")

        elif choice.lower() == "q":
            break

        else:
            # Seems like more than one speak calls dont work
            speak("Invalid choice. Press 1 for tutorial, 2 to play, or Q to quit.")
