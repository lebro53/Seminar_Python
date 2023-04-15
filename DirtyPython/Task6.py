# ПРОСТЕЙШИЙ КАЛЬКУЛЯТОР
# Написать программу, которая выполняет над двумя вещественными числами
# одну из четырех арифметических операций (сложение, вычитание, умножение или деление):
# вводим первое число,
# потом операцию
# и второе число
# выводится результат
#
# Программа должна завершаться только по желанию пользователя:
# можно ввести enter и программа закончится, или еще операцию и еще число.
# Но и помним, что на ноль делить нельзя.


value_1 = int(input('Enter first number: '))
mark = input('Enter mark: ')
value_2 = int(input('Enter second number: '))
result = 0
stop_calculator = '+'


if (mark == '+'):
    result = value_1 + value_2
    print(result)
elif (mark == '-'):
    result = value_1 - value_2
    print(result)
elif (mark == '*'):
    result = value_1 * value_2
    print(result)
elif (mark == '/' and value_2 == 0):
    print("Error. Can't divide by zero")
elif (mark == '/' ):
    result = value_1 / value_2
    print(result)
stop_calculator = input('Do you want to continue? +/-: ')
if (stop_calculator != '+'):
    exit(0)

while True:
    mark = input('Enter mark: ')
    value_2 = int(input('Enter second number: '))
    if (mark == '+'):
        result += value_2
        print(result)
        stop_calculator = input('Do you want to continue? +/-: ')
        if (stop_calculator == '+'):
            continue
        else:
            break
    elif (mark == '-'):
        result -= value_2
        print(result)
        stop_calculator = input('Do you want to continue? +/-: ')
        if (stop_calculator == '+'):
            continue
        else:
            break
    elif (mark == '*'):
        result *= value_2
        print(result)
        stop_calculator = input('Do you want to continue? +/-: ')
        if (stop_calculator == '+'):
            continue
        else:
            break
    elif (mark == '/' and value_2 == 0):
        print("Error. Can't divide by zero")
        stop_calculator = input('Do you want to continue? +/-: ')
        if (stop_calculator == '+'):
            continue
        else:
            break
    elif (mark == '/'):
        result /= value_2
        print(result)
        stop_calculator = input('Do you want to continue? +/-: ')
        if (stop_calculator == '+'):
            continue
        else:
            break
