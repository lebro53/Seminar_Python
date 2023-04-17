import random

# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# import random
#
# my_list = []
# for i in range(10):
#     rnd = random.randint(-5,5)
#     my_list.append(rnd)
#
# print(my_list)
# my_set = set(my_list)
# print(my_set)
# print(len(my_set))
#
# Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

# my_list = []
# shift = 2
# for i in range(10):
#     elem_list = random.randint(-10,10)
#     my_list.append(elem_list)
# print(my_list)
# new_list = my_list[-shift:] + my_list[:-shift]
# print(new_list)
#
# Напишите программу для печати всех уникальных
# # значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}


# my_set = set()
# my_dict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {" V ":"S009"}, {" VIII ":"S007"}]
# for items_set in my_dict:
#     for elem in items_set.values():
#         my_set.add(elem)
#
# print(my_set)


# Задача №23. Решение в группах
# Дан словарь, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов словаря, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

my_list = [0, -1, 5, 2, 3, 4, 5, 3, 2, 1, 5]
counter = 0
for i in range(len(my_list) - 1):
    if my_list[i] < my_list[i + 1]:
        counter += 1
print(counter)
