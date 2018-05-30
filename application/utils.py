import os
import random

from .settings import APP_ROOT


def generate_random_band_name():
    with open(os.path.join(APP_ROOT, 'wi_words.txt'), 'r') as file:
        words_list = file.read().split()
        random_word = random.choice(words_list)
    generated_band_name = random_word.replace('wi', 'weed')
    return generated_band_name
