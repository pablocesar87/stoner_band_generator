wi_words = []
with open('words.txt', 'r') as file:
    words = file.read().split()
    for word in words:
        if word.startswith('wi') or word.endswith('wi'):
            wi_words.append(word)

with open('wi_words.txt', 'w') as wi_file:
    for wi_word in wi_words:
        wi_file.write('{}\n'.format(wi_word))
