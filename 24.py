import math

N = int(input())
dp = [0] * (3 + N)
A = [math.inf] * (3 + N)
B = [math.inf] * (3 + N)
C = [math.inf] * (3 + N)

for i in range(3, 3 + N):
    l_ = list(map(int, input().split()))
    A[i] = l_[0]
    B[i] = l_[1]
    C[i] = l_[2]

for i in range(3, 3 + N):
    dp[i] = min(dp[i - 1] + A[i], dp[i - 2] + B[i - 1],
                dp[i - 3] + C[i - 2])

print(dp[-1], end='')