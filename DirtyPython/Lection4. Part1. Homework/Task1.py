# 1. Написать функцию, которая принимает на вход строку из рандомных цифр и букв, а возвращает:
#   - строку только из букв
#   - строку только из цифр
#   - сравнить длину строк из цифр и из букв и вернуть ту, которая длиннее


def get_letters(text: str) -> str:
    text_letter = ''
    for elem in range(len(text)):
        if not text[elem].isdigit():
            text_letter += text[elem]
    return text_letter


def get_numbers(text: str) -> str:
    text_num = ''
    for elem in range(len(text)):
        if text[elem].isdigit():
            text_num += text[elem]
    return text_num

def comparsion_len_num_and_letter(num_text: str, letter_text: str) -> None:
    if num_text > letter_text:
        print(f'Строка состоящая из цифр {num_text} больше')
    elif num_text == letter_text:
        print(f'Строка состоящая из цифр {num_text} равна строке из букв {letter_text}')
    else:
        print(f'Строка состоящая из букв {letter_text} больше')


letter = get_letters('qwerty12345')
print(letter)
number = get_numbers('qwerty12345')
print(number)
comparsion_len_num_and_letter(number, letter)
