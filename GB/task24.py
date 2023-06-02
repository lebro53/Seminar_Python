cnt_bushes = 10
cnt_berry_on_branch = []
for i in range(cnt_bushes):
    x = int(input('Enter quantity berry: '))
    cnt_berry_on_branch.append(x)
all_berry = []
for i in range(len(cnt_berry_on_branch)-1):
    x = cnt_berry_on_branch[i+1] + cnt_berry_on_branch[i] + cnt_berry_on_branch[i-1]
    all_berry.append(x)
all_berry.append(cnt_berry_on_branch[-1] + cnt_berry_on_branch[0] + cnt_berry_on_branch[-2])
print(all_berry)
print(max(all_berry))