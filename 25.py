import math
N = int(input())
coords = list(map(int, input().split()))
coords.sort()

dp = [math.inf] * (N)
dp[1] = coords[1] - coords[0]
costs = [0] * N
for i in range(1, len(coords)):
    costs[i - 1] = coords[i] - coords[i - 1]

for i in range(2, N):
    dp[i] = costs[i - 1] + min(dp[i - 1], dp[i - 2])
print(dp[-1], end='')