# Задача 8: Требуется определить,
# можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).
#
# *Пример:*
#
# 3 2 4 -> yes
# 3 2 1 -> no

chocolate_length = int(input('Enter chocolate length: '))
chocolate_width = int(input('Enter chocolate width: '))
chocolate_slice = int(input('Enter chocolate slice: '))
chocolate_area = chocolate_length * chocolate_width
if ((chocolate_slice >= chocolate_width or chocolate_slice >= chocolate_length) and chocolate_slice < chocolate_area):
    if (chocolate_slice % chocolate_width == 0 or chocolate_slice % chocolate_length == 0):
        print('Yes')
    else:
       print('No')
else:
    print('No')
