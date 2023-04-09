# Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

number = int(input('Enter a three-digit number: '))

sum = number%10 + number//10%10 + number//100

print(sum)