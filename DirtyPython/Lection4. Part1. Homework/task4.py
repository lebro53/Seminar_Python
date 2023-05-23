# Функция принимает предложение, вычисляет какой буквы в этом предложении больше
# и возвращает эту букву и процент ее вхождения предложение


def percentage_of_occurrence_letter(text: str):
    text = text.replace(' ', '')
    max_letter = ''
    max_count = 0
    for i in text:
        if text.count(i) > max_count:
            max_count = text.count(i)
            max_letter = i
    percentage_of_occurrence = max_count / len(text) * 100
    print(f'Буква {max_letter} встречается {max_count} раз. Процент вхождения равен {round(percentage_of_occurrence, 2)}%')


percentage_of_occurrence_letter('С головы сорвал ветер мой колпак,Я хотел любви, но вышло всё не так,')
