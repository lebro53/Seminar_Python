path = 'sample.txt'
repath = 'sample2.txt'
with open(path, 'r', encoding='UTF-8') as file:
    text = file.readlines()

new_text = [i.capitalize() for i in text]

with open(repath, 'w', encoding='UTF-8') as save_file:
    save_file.write(str(new_text))
