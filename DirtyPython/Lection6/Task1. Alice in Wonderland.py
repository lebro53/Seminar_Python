import string

with open('Alice_in_Wonderland.txt', 'r', encoding='UTF-8') as file:
    text_alice = file.read()
for sym in string.punctuation + "\n\xa01234567890«»-–„":
    text_alice = text_alice.replace(sym, " ")
words = text_alice.split()
dict_words = {word: words.count(word) for word in set(words) if len(word) > 4}
sorted_tuples = sorted(dict_words.items(), key=lambda el: el[1])
print(sorted_tuples[-5:])

