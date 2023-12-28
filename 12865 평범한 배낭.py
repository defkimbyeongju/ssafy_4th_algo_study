N, K = map(int, input().split()) 
items = [tuple(map(int, input().split())) for _ in range(N)]  

dp = [0] * (K + 1)

for weight, value in items:
    for j in range(K, weight - 1, -1):
        dp[j] = max(dp[j], dp[j - weight] + value)

print(dp[K])


# N, K = map(int, input().split()) 
# items = [tuple(map(int, input().split())) for _ in range(N)]  

# dp = [[0] * (K + 1) for _ in range(N + 1)]

# for i in range(1, N + 1):
#     weight, value = items[i - 1]
#     for j in range(1, K + 1):
#         if j < weight:
#             dp[i][j] = dp[i - 1][j]
#         else:
#             dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)

# print(dp[N][K])