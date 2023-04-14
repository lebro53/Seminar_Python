# а) на вход подается слово - проверить, является ли оно палиндромом
# Например на слово  ‘довод’ выводит  ‘да’, а на слово  ‘повод’ - нет.
# Больше примеров слов-палиндромов
# довод, доход, заказ, кабак, комок, мадам, олололо, потоп, радар

text = input(' Enter string to check: ')
if (text == text[::-1]):
    print('Yes. This text is a polindrom')
else:
    print('No. This text is not a polindrom')

# на вход подается фраза - проверить, является ли она палиндромом
# Не учитывается регистр, знаки препинания и пробелы.
# Примеры фраз-палиндромов
# А роза упала на лапу Азора

text = input(' Enter string to check: ')
if (text.lower().replace(' ', '') == text.lower().replace(' ', '')[::-1]):
    print('Yes. This text is a polindrom')
else:
    print('No. This text is not a polindrom')