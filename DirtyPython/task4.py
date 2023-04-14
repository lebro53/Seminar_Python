# 4. СПОРТСМЕНЫ
# На вход подается возраст и вес спортсмена. Вывести группу по возрасту и весовую категорию,
# в которой он будет принимать участие согласно следующим правилам.
# Соревнования юношей младшей возрастной группы (14—15 лет) проводятся без деления участников на весовые категории.
# Соревнования для юношей старшего возраста (16—17 лет) проводятся в весовых категориях:
# легчайшая - до 52 кг
# легкая - до 57
# средняя - до 70
# тяжёлая - до 80
# вторая тяжелая свыше 80
# Соревнования для юниоров (18—19 лет) и взрослых (20 лет и старше)
# легчайшая - до 54 кг
# легкая - до 60
# средняя - до 75
# тяжелая свыше 81
# Лица младше 14 или весом ниже 44 кг до соревнований не допускаются

athlete_age = int(input("Enter athlete's age: "))
athlete_weight = int(input("Enter athlete's weight: "))

if (athlete_age < 14 or athlete_weight < 44):
    print('Sorry. Grow or gain weight')
elif (14 <= athlete_age < 16):
    print('You have junior category!')
elif (16 <= athlete_age < 18):
    if (athlete_weight < 52):
        print('You have middel age and feather-weight category')
    elif (52 <= athlete_weight < 57):
        print('You have middel age and light weight category')
    elif (57 <= athlete_weight < 70):
        print('You have middel age and middel weight category')
    elif (70 <= athlete_weight < 80):
        print('You have middel age and cruiser weight category')
    elif (80 <= athlete_weight):
        print('You have middel age and heavy category')
elif (18 <= athlete_age < 20):
    if (athlete_weight < 54):
        print('You have odd middel age and feather-weight category')
    elif (54 <= athlete_weight < 60):
        print('You have odd middel age and light weight category')
    elif (60 <= athlete_weight < 75):
        print('You have odd middel age and middel weight category')
    elif (75 <= athlete_weight):
        print('You have odd middel age and heavy category')
else:
    if (athlete_weight < 54):
        print('You have senior age and feather-weight category')
    elif (54 <= athlete_weight < 60):
        print('You have senior age and light weight category')
    elif (60 <= athlete_weight < 75):
        print('You have senior age and middel weight category')
    elif (75 <= athlete_weight):
        print('You have senior age and heavy category')