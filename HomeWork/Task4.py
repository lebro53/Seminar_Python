# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок,
# если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10
# a + b + (a + b) * 2 = 60
# 3 * a + 3 * b = 60
# a + b = 20


sum_ships = int(input('Enter number of ships: '))

if (sum_ships % 3 == 0):
    boys_ships = sum_ships // 3
    kate_ships = boys_ships * 2
    print(f'Ships Kate: {kate_ships}, Petr: {boys_ships//2} and Sergey: {boys_ships//2}')
else:
    print('Please enter another number')


