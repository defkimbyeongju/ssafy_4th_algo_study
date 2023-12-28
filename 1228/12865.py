N, K = map(int, input().split())
dp = [0 for _ in range(K+1)]
for _ in range(N):
    W, V = map(int, input().split())
    for i in range(K, W-1, -1):
        dp[i] = max(dp[i], dp[i - W] + V)
print(dp[-1])


# N, K = map(int, input().split())
# arr = []
# for _ in range(N):
#     W, V = map(int, input().split())
#     arr.append([W, V])
# answer = 0

# def f(weight, value, level):
#     global answer
#     if level == N:
#         answer = max(answer, value)
#         return
#     w, v = arr[level]
#     if weight + w > K:
#         answer = max(answer, value)
#         return
#     else:
#         f(weight + w, value + v, level + 1)
#     f(weight, value, level + 1)

# f(0, 0, 0)
# print(answer)
# print(2 ** 100)