# number = int(input('Enter number: '))
# i = 1
# result = 1
# while (i <= number):
#     result *= i
#     i+=1
# print(result)

# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6
# 0 1 1 2 3 5 8 13 21 34 55 89

# fib_number = int(input('Enter number: '))
# fib_1 = 0
# fib_2 = 1
# i = 1
# while (i <= fib_number):
#     fib_sum = fib_1 + fib_2
#     fib_1 = fib_2
#     fib_2 = fib_sum
#     i += 1
#     if fib_sum == fib_number:
#         print(i + 1)
#         exit(0)
# print('This is number not found')

# Задача №13. Решение в группах
# Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в
# свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период, в
# который среднесуточная температура ежедневно превышала
# 0 градусов Цельсия. Напишите программу, помогающую
# синоптикам в работе.
# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2

# import random
#
# quantity_day = 30
# today = 0
# count = 0
# number_warm_days = 0
# max_warm_day = 0
# while (count < quantity_day):
#     today += random.randint(-3, 3)
#     if (today > 0):
#         quantity_warm_day = number_warm_days + 1
#         number_warm_days += 1
#         if (max_warm_day < quantity_warm_day):
#             max_warm_day = quantity_warm_day
#     else:
#         number_warm_days = 0
#     count += 1
#     print(today, end=" ")
# print(f'Оттепель составляет: {max_warm_day} дней')


# Задача №15. Решение в группах
# 15. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

import random

quantity_watermelon = 10
watermelon_weight = 0
count = 0
max_weight_watermelon = 0
min_weight_watermelon = 5
while (count < quantity_watermelon):
    watermelon_weight = random.randint(1, 15)
    print(watermelon_weight, end=' ')
    if (max_weight_watermelon < watermelon_weight):
        max_weight_watermelon = watermelon_weight
    if (watermelon_weight < min_weight_watermelon):
        min_weight_watermelon = watermelon_weight
    count += 1
print(end='\n')
print(max_weight_watermelon, min_weight_watermelon)
