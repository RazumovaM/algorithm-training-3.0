N, M = list(map(int, input().split()))

dp = [[0 for _ in range(N)] for _ in range(M)]

if N >= 3:
    dp[1][2] = 1
if M >= 3:
    dp[2][1] = 1
for i in range(2, M):
    for j in range(2, N):
        dp[i][j] = dp[i - 2][j - 1] + dp[i - 1][j - 2]

if N == M == 1:
    print(1)
else:
    print(dp[-1][-1])
