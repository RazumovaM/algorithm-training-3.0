import math

N = int(input())
price = [0] * N
for i in range(N):
    price[i] = int(input())

dp_result = [[math.inf for _ in range(N + 2)] for _ in range(N + 1)]
dp_result[0][0] = 0
max_ind = 0
for j in range(1, N + 1):
    for i in range(0, N + 1):
        if i == 0:
            dp_result[j][i] = min(dp_result[j-1][i + 1], dp_result[j-1][i] + price[j - 1])
        else:
            if price[j - 1] <= 100:
                dp_result[j][i] = min(dp_result[j-1][i + 1], dp_result[j-1][i] + price[j - 1])
            else:
                dp_result[j][i] = min(dp_result[j-1][i - 1] + price[j - 1], dp_result[j-1][i + 1])

print(min(dp_result[-1]))
dp_result[-1].reverse()
i_ind_min = len(dp_result[-1]) - dp_result[-1].index(min(dp_result[-1])) - 1

print(i_ind_min, end=' ')
dp_result[-1].reverse()
l_result = list()
N_used = 0
for j in range(N, 1, -1):
    if dp_result[j - 1][i_ind_min + 1] == dp_result[j][i_ind_min] and dp_result[j - 1][i_ind_min + 1] != math.inf:
        l_result.append(j)
        i_ind_min += 1
        N_used += 1
    elif (dp_result[j - 1][i_ind_min - 1] + price[j - 1] == dp_result[j][i_ind_min]) and price[j - 1] > 100:
        i_ind_min -= 1

print(N_used)
l_result.reverse()
for l in l_result:
    print(l)



