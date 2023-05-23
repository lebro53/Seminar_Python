import string

with open('Alice_in_Wonderland.txt', 'r', encoding='UTF-8') as file:
    text_alice = file.read()

for sym in string.punctuation + "\n\xa01234567890«»-–„":
    text_alice = text_alice.replace(sym, " ")

all_words = text_alice.split()

new_dict = {}

for word in set(all_words):
    if len(word) > 4:
        new_dict[word] = all_words.count(word)

sorted_tuples = sorted(new_dict.items(), key=lambda x: x[1])
print(sorted_tuples[-5:])
