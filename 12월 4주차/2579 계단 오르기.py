def DP(N, arr):
    dp = [0] * N
    dp[0] = arr[0]
    if N > 1:
        dp[1] = arr[0] + arr[1]
        for i in range(2, N):
            dp[i] = max(dp[i], dp[i-2] + arr[i], dp[i-3] + arr[i-1] + arr[i])
    return dp[N-1]

n = int(input())
arr = [int(input()) for _ in range(n)]
print(DP(n, arr))