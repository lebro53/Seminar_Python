# 5. FIZZ BUZZ
# Напишите программу, которая выводит на экран числа от 1 до n.
# При этом вместо чисел, кратных трем, программа должна выводить слово «Fizz»,
# а вместо чисел, кратных пяти — слово «Buzz».
# Если число кратно и 3, и 5, то программа должна выводить слово «FizzBuzz»

number = int(input('Enter number: '))
i = 1
while (i <= number):
    if (i % 3 == 0 and i % 5 == 0):
        print('FizzBuzz')
    elif (i % 3 == 0):
        print('Fizz')
    elif (i % 5 == 0):
        print('Buzz')
    else:
        print(i)
    i += 1
