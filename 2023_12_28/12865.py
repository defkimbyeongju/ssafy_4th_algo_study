import sys
n, k = map(int, sys.stdin.readline().split())
bx = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def recur(idx, weight):
    if weight > k:
        return -1e9

    if idx == n:
        return 0

    if dp[idx][weight] != -1:
        return dp[idx][weight]

    dp[idx][weight] = max(recur(idx+1, weight+bx[idx][0]) + bx[idx][1], recur(idx+1, weight))

    return dp[idx][weight]

dp = [[-1 for _ in range(100100)] for _ in range(n)]
recur(0, 0)
print(dp[0][0])