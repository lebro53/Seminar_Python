# 5. Вводим сегодняшнюю дату и сегодняшний день недели,
# затем вводим новую дату
# программа должна выдать нам какой день недели будет в эту дату



day_dict = {1: 'Четверг', 2: 'Пятница', 3: 'Суббота',
              4: 'Воскресение', 5: 'Понедельник', 6: 'Вторник',
              0: 'Среда'}

start_day = 1
start_month = 1
start_years = 1970
finish_day = 28
finish_month = 4
finish_years = 2023

leap_years = 0
leap_month = 29
day_of_month = 0
quantity_start_day = 0
quantity_finish_day = 0
# Находим количество високосных дней
for i in range(start_years, finish_years+1):
    if i % 400 == 0 or (i % 4 == 0 and i % 100 != 0):
        leap_years += 1

# В идеале нижний цикл надо засунуть в функцию и будет красиво.
#
while start_month > 0:
    if start_month == 1 or start_month == 3 or start_month == 5 or start_month == 7 or start_month == 8 or start_month == 10 or start_month == 12:
        day_of_month = 31
    elif start_month == 2 and (start_years % 400 != 0 or (start_years % 4 != 0 and start_years % 100 == 0)):
        day_of_month = 28
    elif start_month == 2 and (start_years % 400 == 0 or (start_years % 4 == 0 and start_years % 100 != 0)):
        day_of_month = 29
    else:
        day_of_month = 30
    quantity_start_day += day_of_month
    start_month -= 1

while finish_month > 0:
    if finish_month == 1 or finish_month == 3 or finish_month == 5 or finish_month == 7 or finish_month == 8 or finish_month == 10 or finish_month == 12:
        day_of_month = 31
    elif finish_month == 2 and (finish_years % 400 != 0 or (finish_years % 4 != 0 and finish_years % 100 == 0)):
        day_of_month = 28
    elif finish_month == 2 and (finish_years % 400 == 0 or (finish_years % 4 == 0 and finish_years % 100 != 0)):
        day_of_month = 29
    else:
        day_of_month = 30
    quantity_finish_day += day_of_month
    finish_month -= 1


quantity_day = (finish_years - start_years) * 365 + leap_years + quantity_finish_day - (day_of_month - finish_day)



test_key = quantity_day % 7
for key, value in day_dict.items():
    if key == test_key:
        print(value)

