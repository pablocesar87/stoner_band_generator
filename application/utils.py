import os
import random

from .settings import APP_ROOT


vowels = ['a', 'e', 'i', 'o', 'u']
acceptable_consonants = ['sh', 'ch', 'br', 'tr', 'th']


def generate_random_band_name():
    gramatically_wrong = True
    with open(os.path.join(APP_ROOT, 'wi_words.txt'), 'r') as file:
        words_list = file.read().split()
        while gramatically_wrong:
            random_word = random.choice(words_list)
            if random_word.endswith('wi'):
                generated_band_name = random_word.replace('wi', 'weed')
                gramatically_wrong = False
            elif random_word.startswith('wi') and (
                random_word[2] in vowels or random_word[3] in vowels
            ):
                generated_band_name = random_word.replace('wi', 'weed')
                gramatically_wrong = False
            elif random_word.startswith('wi') and random_word[2:3] in (
                acceptable_consonants
            ):
                generated_band_name = random_word.replace('wi', 'weed')
                gramatically_wrong = False
    return generated_band_name


def get_adjetive():
    with open(os.path.join(APP_ROOT, 'adjetives.txt'), 'r') as file:
        adjetives = file.read().split()
    return random.choice(adjetives)
