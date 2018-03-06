import random

words = ['dom', 'samochód', 'komputer', 'praca', 'wieszak', 'zdjęcie']
words_temp = words[:]
random.shuffle(words_temp)

for word in words_temp:
    print(word)
