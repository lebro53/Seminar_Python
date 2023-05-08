# Написать функцию, которая будет возвращать список созданный по
# заданным критериям: размер, минимальное и максимальное
# значение, наличие повторяющихся элементов
import random


def create_list(size: int, min_elem: int, max_elem: int, repeat_elem: bool) -> list[int]:
    new_list = []
    for i in range(size):
        elem = random.randint(min_elem, max_elem)
        new_list.append(elem)
    if not repeat_elem:
        my_set = set(new_list)
        new_list = list(my_set)
    return new_list


my_list = create_list(10, 1, 11, False)
print(my_list)
