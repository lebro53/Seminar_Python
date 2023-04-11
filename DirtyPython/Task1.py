# 1. На вход поступает число: найти сумму цифр числа,
# в том числе если оно отрицательное или вещественное. (float)
#
m = input('Enter number: ')
n = int(float(m) * 10 ** len(m))
print(n)
a = 0
if (n >= 0):
    for i in range(len(m) * 2):
        a += n % 10
        n = n // 10
    print(a)
else:
    n = n * -1
    for i in range(len(m) * 2):
        a += n % 10
        n = n // 10
    print(a)
