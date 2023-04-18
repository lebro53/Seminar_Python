# 1. Для разминки. Дан список чисел.
# Создать новый список,
# который будет содержать только уникальные элементы исходного списка
import random

my_list = [random.randint(1,10) for i in range(20)]
unique_set = set(my_list)
print(my_list)
print(unique_set)