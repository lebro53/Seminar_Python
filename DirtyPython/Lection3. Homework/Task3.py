# у нас есть шахматная доска. по горизонтали
# нумерована цифрами, по вертикали буквами. написать
# программу, которая определяет цвет клетки по ее
# координатам(например B7 = Белая), если точно знаем, что клетка А1 - черная
letter_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
numbers_list = ['1', '2', '3', '4', '5', '6', '7', '8']
board_list = []
black_list = []
white_list = []
search = input('Enter the desired cell: ').upper()
flag = True
for item_letter in letter_list:
    for item_numbers in numbers_list:
        board_list.append(item_letter + item_numbers)

for i in range(len(board_list) - 56):
    if i % 2 == 0:
        black_list.append(board_list[i])
    else:
        white_list.append(board_list[i])

for i in range(8, len(board_list) - 48):
    if i % 2 != 0:
        black_list.append(board_list[i])
    else:
        white_list.append(board_list[i])
for i in range(16, len(board_list) - 40):
    if i % 2 == 0:
        black_list.append(board_list[i])
    else:
        white_list.append(board_list[i])
for i in range(24, len(board_list) - 32):
    if i % 2 != 0:
        black_list.append(board_list[i])
    else:
        white_list.append(board_list[i])
for i in range(32, len(board_list) -24):
    if i % 2 == 0:
        black_list.append(board_list[i])
    else:
        white_list.append(board_list[i])
for i in range(40, len(board_list) - 16):
    if i % 2 != 0:
        black_list.append(board_list[i])
    else:
        white_list.append(board_list[i])
for i in range(48, len(board_list) - 8):
    if i % 2 == 0:
        black_list.append(board_list[i])
    else:
        white_list.append(board_list[i])
for i in range(56, len(board_list) ):
    if i % 2 != 0:
        black_list.append(board_list[i])
    else:
        white_list.append(board_list[i])

for i in black_list:
    if search == i:
        flag = False
if flag == False:
    print('Black')
else:
    print('White')