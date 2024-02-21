import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0]*3 for _ in range(N)] for _ in range(N)]
dp[0][1][0] = 1
for i in range(2,N):
    if arr[0][i] == 0:
        dp[0][i][0] = dp[0][i-1][0]

for i in range(1,N):
    for j in range(2, N):
        for k in range(3):
            if k== 0:
                if arr[i][j] == 0:
                    dp[i][j][k] = dp[i][j-1][0] + dp[i][j-1][1]
            elif k == 1:
                if arr[i][j-1] == arr[i-1][j] == arr[i][j] == 0:
                    dp[i][j][k] = dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2]
            else:
                if arr[i][j] == 0:
                    dp[i][j][k] = dp[i-1][j][1] + dp[i-1][j][2]
print(sum(dp[N-1][N-1]))