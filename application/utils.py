import random


def generate_random_band_name():
    with open('application/wi_words.txt', 'r') as file:
        words_list = file.read().split()
        random_word = random.choice(words_list)
    generated_band_name = random_word.replace('wi', 'weed')
    return generated_band_name
