import numpy as np
import sounddevice as sd

SAMPLE_RATE = 44100

def tone(freq, duration=0.45):
    t = np.linspace(0, duration, int(SAMPLE_RATE*duration), False)
    wave = 0.25*np.sin(2*np.pi*freq*t)
    return wave.astype(np.float32)

def play_array(arr):
    sd.play(arr, SAMPLE_RATE, blocking=True)

KEY_FREQS = {
    '1': 261.63,  # C4
    '2': 329.63,  # E4
    '3': 392.00,  # G4
    '4': 523.25,  # C5
    '5': 659.25,  # E5
    '6': 783.99   # G5
}

def play_key(key):
    if key in KEY_FREQS:
        play_array(tone(KEY_FREQS[key]))

def success():
    play_array(tone(880, 0.2))

def fail():
    play_array(tone(110, 0.4))
