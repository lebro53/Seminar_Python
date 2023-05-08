# 3. функцию для проверки числа:
#   - четность - нечетность
#   - простое число (имеет всего два делителя - само себя и единицу)
#   - сумма всех цифр числа является делителем этого числа
#   - *принимает число и выдает его только простые делители

def check_number(num: int) -> None:
    print(f'Число {num} четное') if num % 2 == 0 else print(f'Число {num} не четное')


def is_prime(num: int) -> bool:
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            return False
    return True


def divider(num: int) -> None:
    number = num
    sum_number = 0
    while number > 0:
        sum_number += number % 10
        number //= 10
    if num % sum_number == 0:
        print('Cумма всех цифр числа является делителем этого числа')
    else:
        print('Cумма всех цифр числа не является делителем этого числа')


def search_is_prime(num: int) -> list[int]:
    new_list = []
    not_now_list = []
    for j in range(1, num+1):
        if num % j == 0:
            new_list.append(j)
            for i in range(2, (j // 2) + 1):
                if j % i == 0:
                    not_now_list.append(j)
    new_list = list(set(new_list)-set(not_now_list))
    new_list.sort()
    return new_list


print(search_is_prime(3859152))

# divider(23)
#
# if is_prime(57):
#     print('Yes')
# else:
#     print('No')
