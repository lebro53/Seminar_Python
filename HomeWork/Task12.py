# Задача 12: Петя и Катя – брат и сестра.
# Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать.
# Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.


import math

sum_numbers = int(input('Enter sum numbers: '))
product_numbers = int(input('Enter product numbers: '))
discriminant = sum_numbers * sum_numbers - 4 * product_numbers
if (discriminant < 0):
    print('No solution')
elif (discriminant == 0):
    second_number = sum_numbers / 2
    first_number = sum_numbers - second_number
    print(f'First number = {int(first_number)}, second number = {int(second_number)}')
else:
    second_number = (sum_numbers + discriminant ** 0.5) / 2
    first_number = (sum_numbers - discriminant ** 0.5) / 2
    print(int(first_number), int(second_number))

