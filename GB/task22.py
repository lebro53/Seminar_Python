import random

num1 = [random.randint(1, 15) for i in range(10)]
num2 = [random.randint(1, 15) for i in range(10)]
num3 = [i for i in num2 if i in num1]
num3.sort()
print(num2)
print(num1)
print(num3)