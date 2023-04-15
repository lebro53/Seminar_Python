# 3. ИСТИННОСТЬ ПРЕДИКАТ
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# Данное выражение истинно при любых значениях предикат
# (предикат - переменная, которая может иметь только два значения True или False)
# Напишите программу, которая докажет это.

x = int(input('Enter value x = 1 or 0: '))
y = int(input('Enter value y = 1 or 0: '))
z = int(input('Enter value z = 1 or 0: '))

if (x == 1):
    x = True
else:
    x = False
if (y == 1):
    x = True
else:
    x = False
if (z == 1):
    x = True
else:
    x = False
print(not (x * y * z) == (not x) + (not y) + (not z))
