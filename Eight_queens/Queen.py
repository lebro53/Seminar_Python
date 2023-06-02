alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
number = [1, 2, 3, 4, 5, 6, 7, 8]
left_list = []
right_list = []
queen = {'q1': '', 'q2': '', 'q3': '', 'q4':'', 'q5': '', 'q6': '', 'q7': '', 'q8':''}






def left_triander(alpha: list, num: list):
    num_l = 0
    count_l = 0
    for i in num:
        while count_l <= num_l:
            left_list.append(str(i) + alpha[count_l])
            print(f'{str(i) + alpha[count_l] :<3}', end='')
            count_l += 1
        count_l = 0
        num_l += 1
        print()


def right_triander(alpha: list, num: list):
    alpha.reverse()
    num.reverse()
    num_l = 0
    count_l = 0
    for i in num:
        while count_l <= num_l:
            right_list.append(str(i) + alpha[count_l])
            print(f'{str(i) + alpha[count_l] :<3}', end='')
            count_l += 1
        count_l = 0
        num_l += 1
        print()


left_triander(alphabet, number)
# right_triander(alphabet, number)
print(left_list)