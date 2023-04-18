# 4. Принимаем с консоли число и выводим две последовательности Фибоначчи
# и Негафибоначчи (можно прочитать в wiki что это)
# Пример: Вводим 8
# [-21, 13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

fib_numbers = 7
neg_fib_1 = fib_1 = 0
neg_fib_2 = fib_2 = 1
sum_neg_fib = sum_fib = 0
i = 0
feb_list = []
neg_feb_list = []
sum_neg_and_feb_list = []
while fib_numbers > 0:
    feb_list.append(sum_fib)
    sum_fib = fib_1 + fib_2
    fib_1 = fib_2
    fib_2 = sum_fib
    neg_feb_list.append(sum_neg_fib)
    sum_neg_fib = neg_fib_1 - neg_fib_2
    neg_fib_1 = neg_fib_2
    neg_fib_2 = sum_neg_fib
    fib_numbers -= 1

sum_neg_and_feb_list = neg_feb_list[len(neg_feb_list):1:-1] + feb_list
print(sum_neg_and_feb_list)
