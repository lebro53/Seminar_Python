alphabet = [i for i in 'абвгдеёжзийклмнопрстуфхцчшщьъэюя .,!?:;()']
number_of_letters = len(alphabet)
numerate = [i for i in range(number_of_letters)]
alphabet_dict = dict(zip(numerate, alphabet))
print(alphabet_dict)

text = input('Введите текст для шифрования?: ').lower()
shift = int(input('Введите длину сдвига: '))


def caesar_cipher(entered_text: str, entered_shift: int, quantity_letters: int, dict_for_cipher: dict) -> str:
    temporary_list = []
    for i in entered_text:
        for key, values in dict_for_cipher.items():
            if i == values:
                if key + entered_shift >= quantity_letters:
                    i = dict_for_cipher.get(key + entered_shift - quantity_letters)
                else:
                    i = dict_for_cipher.get(key + entered_shift)
                temporary_list.append(i)
                break
    cipher_text = ''.join(temporary_list)
    return cipher_text


def caesar_decipher(entered_text: str, entered_shift: int, quantity_letters: int, dict_for_cipher: dict) -> str:
    detemporary_list = []
    for i in entered_text:
        for key, values in dict_for_cipher.items():
            if i == values:
                if key - entered_shift < 0:
                    i = dict_for_cipher.get(key - entered_shift + quantity_letters)
                else:
                    i = dict_for_cipher.get(key - entered_shift)
                detemporary_list.append(i)
                break
    decipher_text = ''.join(detemporary_list)
    return decipher_text


new_text = caesar_cipher(text, shift, number_of_letters, alphabet_dict)
print(new_text)
decip_text = caesar_decipher(new_text, shift, number_of_letters, alphabet_dict)
print(decip_text)