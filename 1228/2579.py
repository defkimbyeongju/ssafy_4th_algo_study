N = int(input())
dp = [0] * (N+1)
stairs = [0]
for _ in range(N):
    p = int(input())
    stairs.append(p)
dp[1] = stairs[1]
if N > 1:
    dp[2] = sum(stairs[1:3])
for i in range(3, N+1):
    dp[i] = max(dp[i-2], stairs[i-1] + dp[i-3]) + stairs[i]
print(dp[N])