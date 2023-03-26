N, M = list(map(int, input().split()))
list_ = [0] * N

for n in range(N):
    list_[n] = list(map(int, input().split()))

dp = [[0] * (M + 1)] * (N + 1)
result = [0] * (N + 1)
result[0] = [0] * (M + 1)
for i in range(1, N + 1):
    for j in range(1, M + 1):
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + list_[i - 1][j - 1]
    result[i] = dp[i][:]

i = -1
j = -1
result_list = list()
n = N + M - 2
while n > 0:
    if result[i - 1][j] > result[i][j - 1]:
        n -= 1
        i -= 1
        result_list.append('D')
    elif result[i - 1][j] < result[i][j - 1]:
        n -= 1
        j -= 1
        result_list.append('R')
    elif result[i - 1][j] == result[i][j - 1]:
        n -= 1
        i -= 1
        result_list.append('D')

print(dp[-1][-1])
result_list.reverse()
print(' '.join(result_list), end='')





