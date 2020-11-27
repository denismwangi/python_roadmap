from random import shuffle
word = input('enter a word')

letter_list = list(word)
shuffle(letter_list)
anagramm = ''.join(letter_list)
print(anagramm)