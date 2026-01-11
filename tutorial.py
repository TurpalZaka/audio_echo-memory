import time
from audio import play_key, success, fail, KEY_FREQS
from speech import speak


def run_tutorial(get_key_fn, num_keys: int = 4):
    """
    Interactive tutorial to learn the mapping between tones and keys.

    - Uses audio tones and spoken instructions.
    - Adapts to difficulty: num_keys can be 4, 5, or 6.
    - get_key_fn is a function that returns a validated key press as a string.
    """

    # Clamp to safe range and ensure we don't exceed available frequencies
    num_keys = max(4, min(6, int(num_keys)))
    available_keys = list(KEY_FREQS.keys())[:num_keys]  # e.g. ['1','2','3','4'] or up to '6'

    key_range_text = f"keys 1 to {available_keys[-1]}"

    speak(
        "Tutorial mode. "
        f"You will learn the sounds for {key_range_text}. "
        "After each tone, press the matching key on your keyboard and press Enter."
    )

    print(f"Tutorial: Learn {key_range_text}.")
    print(f"After each tone, type the key you think it is (1-{available_keys[-1]}) and press Enter.")

    for k in available_keys:
        msg = f"Now learning key {k}. Listen to the tone, then press {k}."
        print(msg)
        speak(msg)

        while True:
            # Play the reference tone
            play_key(k)
            time.sleep(0.15)

            pressed = get_key_fn()

            if pressed == k:
                success()
                print(f"Correct: that was key {k}.")
                speak(f"Correct. That was key {k}.")
                break
            else:
                fail()
                print(f"Wrong key ({pressed}). Try again.")
                speak("Wrong key. Try again.")

    print(f"\nTutorial completed. You now know the tones for {key_range_text}.")
    speak(f"Tutorial completed. You now know the tones for {key_range_text}.")
    return True
