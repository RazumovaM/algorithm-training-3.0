list_ = list(map(int, input().split()))
N = list_[0]
k = list_[1]

dp = [0] * (N + k - 1)
if k == 1:
    dp[0] = 1
else:
    for i in range(k):
        dp[i] = 0
    dp[k - 1] = 1
for i in range(k, k + N - 1):
    for k_ in range(k + 1):
        dp[i] += dp[i - k_]
print(dp[-1], end='')