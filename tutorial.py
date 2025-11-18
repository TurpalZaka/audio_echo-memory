import time
from audio import play_key, success, fail, KEY_FREQS
from speech import speak


def run_tutorial(get_key_fn):
    """
    Interactive tutorial to learn the mapping between tones and keys 1-4.
    Uses both audio tones and spoken instructions.
    """
    speak(
        "Tutorial mode. "
        "You will learn the sounds for keys 1, 2, 3 and 4"
        "After each tone, press the matching key on your keyboard and press Enter."
    )

    print("Tutorial: Learn keys 1-4.")
    print("After each tone, type the key you think it is (1-4) and press Enter.")

    order = list(KEY_FREQS.keys())  # typically ['1', '2', '3', '4']

    for k in order:
        msg = f"\nNow learning key {k}. Listen to the tone, then press {k}."
        print(msg)
        speak(f"Now learning key {k} Listen to the tone, then press {k}")

        while True:
            # Play the reference tone
            play_key(k)
            time.sleep(0.15)

            pressed = get_key_fn()

            if pressed == k:
                success()
                print(f"Correct: that was key {k}.")
                speak(f"Correct. That was key {k}")
                break
            else:
                fail()
                print(f"Wrong key ({pressed}). Try again.")
                speak("Wrong key. Try again.")

    print("\nTutorial completed. You now know the tones for keys 1-4.")
    speak("Tutorial completed. You now know the tones for keys 1, 2, 3 and 4")
    return True
