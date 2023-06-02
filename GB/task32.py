arg = [i for i in range(1, 10)]
for i in range(len(arg)):
    if 3 < arg[i] <= 7:
        print(f'Елемент {arg[i]} с индексом {i}')
