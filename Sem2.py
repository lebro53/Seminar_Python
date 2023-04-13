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

fib_number = int(input('Enter number: '))
fib_1 = 0
fib_2 = 1
i = 1
while (i <= fib_number):
    fib_sum = fib_1 + fib_2
    fib_1 = fib_2
    fib_2 = fib_sum
    i += 1
    if fib_sum == fib_number:
        print(i+1)
        exit(0)
print('This is number not found')

