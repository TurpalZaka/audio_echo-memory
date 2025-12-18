import random, time
from audio import play_key, success, fail, KEY_FREQS
from storage import load_highscore, save_highscore

# Global settings (set from main.py)
PROFILE = 1     # 1..4
NUM_KEYS = 4    # 4..6

def configure(profile: int, num_keys: int):
    global PROFILE, NUM_KEYS
    PROFILE = max(1, min(4, int(profile)))
    NUM_KEYS = max(4, min(6, int(num_keys)))

class Game:
    def __init__(self):
        self.sequence = []
        self.score = 0
        self.high = load_highscore(PROFILE)

        # only allow first NUM_KEYS keys (1..4, 1..5, or 1..6)
        all_keys = list(KEY_FREQS.keys())  # expects '1'..'6'
        self.allowed = all_keys[:NUM_KEYS]

    def new_round(self):
        self.sequence.append(random.choice(self.allowed))
        for k in self.sequence:
            play_key(k)
            time.sleep(0.15)

    def input_phase(self, get_key_fn):
        for k in self.sequence:
            pressed = get_key_fn()
            if pressed != k:
                fail()
                self.finish()
                return False
        success()
        self.score += 1
        return True

    def finish(self):
        if self.score > self.high:
            self.high = self.score
            save_highscore(PROFILE, self.high)

def play_loop(get_key_fn):
    g = Game()
    keep = True
    while keep:
        g.new_round()
        keep = g.input_phase(get_key_fn)
    return g.score, g.high
