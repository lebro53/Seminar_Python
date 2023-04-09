# Задача 6: Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
#
# *Пример:*
#
# 385916 -> yes
# 123456 -> no

number_ticket = int(input('Enter number of ticket: '))

first_half_number_ticket = number_ticket//1000 % 10 + number_ticket // 10000 % 10 + number_ticket // 100000
second_half_number_ticket = number_ticket % 10 + number_ticket // 10 % 10 + number_ticket // 100 % 10
if(first_half_number_ticket == second_half_number_ticket):
    print('Congratulation. This is a lucky ticket')
else:
    print('This ticket is not happy')

