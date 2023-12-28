N, K = map(int, input().split()) 
items = [tuple(map(int, input().split())) for _ in range(N)]  

dp = [0] * (K + 1)

for weight, value in items:
    for j in range(K, weight - 1, -1):
        dp[j] = max(dp[j], dp[j - weight] + value)

print(dp[K])
