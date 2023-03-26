N = int(input())


dp = [0] * N
if N == 1:
    print(2)
elif N == 2:
    print(4)
elif N == 3:
    print(7)
else:
    dp[0] = 2
    dp[1] = 4
    dp[2] = 7
    for i in range(3, N):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    print(dp[-1])