# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5


my_list = [i for i in range(1, 20)]
check_number = 21
print(my_list)
minimum_elem = 1
for i in range(len(my_list)):
    if my_list[i] == check_number and i != 0:
        minimum_elem = my_list[i-1]
    elif my_list[i] == check_number and i == 0:
        minimum_elem = None
    elif my_list[i] < check_number and minimum_elem != None:
        minimum_elem = my_list[len(my_list)-1]
if minimum_elem == None:
    print('Ближайшего числа нет')
else:
    print(minimum_elem)




