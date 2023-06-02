path = 'RLE_Text.txt'
with open(path, 'r', encoding='UTF-8') as file:
    text = file.read()


def number_or_letter(word: str) -> bool:
    for i in word:
        if i.isdigit():
            return True
    return False


def package(word: str) -> str:
    num_str = ''
    letter_str = ''
    count_letter = 1
    for i in word:
        if i != letter_str:
            if letter_str:
                num_str += str(count_letter) + letter_str
            count_letter = 1
            letter_str = i
        else:
            count_letter += 1
    else:
        num_str += str(count_letter) + letter_str
        return num_str


def unpacking(word: str) -> str:
    num_str = ''
    letter_str = ''
    for i in word:
        if i.isdigit():
            num_str += i
        else:
            letter_str += int(num_str) * i
            num_str = ''
    return letter_str


print(number_or_letter(text))