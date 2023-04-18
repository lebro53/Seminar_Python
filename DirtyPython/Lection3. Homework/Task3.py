# у нас есть шахматная доска. по горизонтали
# нумерована цифрами, по вертикали буквами. написать
# программу, которая определяет цвет клетки по ее
# координатам(например B7 = Белая), если точно знаем, что клетка А1 - черная
letter_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
numbers_list = ['1', '2', '3', '4', '5', '6', '7', '8']
black_list = []
white_list = []
search = input('Enter the desired cell: ').upper()
black_flag = 0
white_flag = 0

for i in range(len(letter_list)):
    for j in range(len(numbers_list)):
        if i % 2 != 0:
            if j % 2 != 0:
                black_list.append(letter_list[i] + numbers_list[j])
            else:
                white_list.append(letter_list[i] + numbers_list[j])
        else:
            if j % 2 == 0:
                black_list.append(letter_list[i] + numbers_list[j])
            else:
                white_list.append(letter_list[i] + numbers_list[j])

for i in black_list:
    if search == i:
        black_flag = 1

for i in white_list:
    if search == i:
        white_flag = 1

if black_flag == 1:
    print(f'{search} = Black')
elif white_flag == 1:
    print(f'{search} = White')
else:
    print('Not found')
