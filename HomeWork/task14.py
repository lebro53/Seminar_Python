# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k),
# не превосходящие числа N.
degree = int(input('Enter degree of: '))
count = 1
number = 2
while (count < degree):
    degree_number = number ** count
    print(degree_number)
    count += 1

