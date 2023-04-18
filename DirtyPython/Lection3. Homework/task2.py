# 2. Мы уже делали переводчик числа из десятичной в двоичную в двоичную,
# время сделать для восьмиричной и шестнадцатиричной.
# а лучше сделать универсальный (двоичная, восьмиричная, шеснадцатиричная)
# и подумать как интереснее оформить "меню" выбора в какую систему переводим:)

convert = int(input('Select number system 2, 8 or 16: '))
number = int(input('Enter the number you want to convert: '))
binary = ''
if convert == 2:
    while number:
        binary = str(number % 2) + binary
        number //= 2
elif convert == 8:
    while number:
        binary = str(number % 8) + binary
        number //= 8
elif convert == 16:
    while number:
        binary = str(number % 16) + binary.replace('10', 'A').replace('11','B').replace('12','C').replace('13','D').replace('14','E').replace('15','F')
        number //= 16

print(binary)
