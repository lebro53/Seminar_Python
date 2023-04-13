# Задача 10: На столе лежат n монеток.
# Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

import random

quantity_coin = 10
count = 0
eagle = 0
tails = 0

while (count < quantity_coin):
    coin = random.randint(0, 1)
    if (coin == 0):
        eagle += 1
    else:
        tails += 1
    count += 1

print(f'Eagle up : {eagle}, tails up: {tails}')
if (eagle > tails):
    print(f'Quantity of coin needed turn over = {quantity_coin - eagle}')
else:
    print(f'Quantity of coin needed turn over = {quantity_coin - tails}')
