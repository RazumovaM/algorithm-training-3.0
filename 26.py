import math
N, M = list(map(int, input().split()))
list_ = [0] * N

for n in range(N):
    list_[n] = list(map(int, input().split()))

dp = [[math.inf] * (M + 1)] * (N + 1)
result = [math.inf] * (N + 1)
result[0] = [math.inf] * (M + 1)
for i in range(1, N + 1):
    for j in range(1, M + 1):
        if i == 1 and j == 1:
            dp[i][j] = list_[0][0]
        else:
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + list_[i - 1][j - 1]
    result[i] = dp[i][:]

print(dp[-1][-1], end='')





