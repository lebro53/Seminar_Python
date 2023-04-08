'''За день машина проезжает n километров.
Сколько дней нужно, чтобы проехать маршрут длиной m километров?
При решении этой задачи нельзя пользоваться
условной инструкцией if и циклами.'''


n = int(input('Введите сколько машина проезжает за 1 день: '))
m = int(input('Введите полное расстояние: '))


average_speed = n/24
full_time_hours = m/average_speed
full_day = int(full_time_hours//24)
hours_float = full_time_hours % 24
hours_int = int(full_time_hours % 24)
coefficient = hours_int * 60
minutes = int(hours_float * 10 * 6-coefficient)

print(f'Количество времени которое понадобится для проезда расстояния {m} км равно {full_day} день/ней {hours_int} часов {minutes} минут')