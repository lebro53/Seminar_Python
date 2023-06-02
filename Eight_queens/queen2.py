alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
number = [1, 2, 3, 4, 5, 6, 7, 8]
queen = {'q1': 'C2', 'q2': '', 'q3': '', 'q4': '', 'q5': '', 'q6': '', 'q7': '', 'q8': ''}
number.reverse()
# deck = []
q1 = []
q2 = []
q3 = []
q4 = []
q5 = []
q6 = []
q7 = []
q8 = []
for j in range(len(number)):
    for i in alphabet:
        # deck.append(i + str(number[j]))
        print(f'{i + str(number[j]):<3}', end='')
    print()
#
# for j in range(len(number)):
#     for i in range(len(alphabet)):
#         if queen['q1'] == str(alphabet[0]) + str(number[0]):
#             queen['q2'] = str(alphabet[0]) + str(number[len(number) - 1])
#             queen['q3'] = str(alphabet[len(alphabet) - 1]) + str(number[0])
#             queen['q4'] = str(alphabet[len(alphabet) - 1]) + str(number[len(number) - 1])
#
#     # print()
# print(queen)


# def destroy(queen1:list):
for j in range(len(number)):
    for i in range(len(alphabet)):
        if queen['q1'] == alphabet[i] + str(number[j]):
            _ = i
            for num in number:
                q1.append(alphabet[i] + str(num))
            for alp in alphabet:
                q1.append(alp + str(number[j]))
            # j = len(number)
            while i >= 0:
                q1.append(alphabet[i] + str(number[j]))
                i -= 1
                j -= 1
            # while i <= _:
            #     q1.append(alphabet[i] + str(number[j]))
            #     i += 1
            #     j += 1

print(q1)
