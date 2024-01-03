a = input()
b = input()

dp = [[0 for _ in range(len(b)+1)] for _ in range(len(a)+1)]
dp2 = [['' for _ in range(len(b)+1)] for _ in range(len(a)+1)]

for i in range(len(a)+1):
    for j in range(len(b)+1):
        if i == 0 or j == 0:
            dp[i][j] = 0
            dp2[i][j] = ''
        elif a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            dp2[i][j] = dp2[i-1][j-1] + b[j-1]
        else:
            if dp[i][j-1] > dp[i-1][j]:
                dp[i][j] = dp[i][j-1]
                dp2[i][j] = dp2[i][j-1]
            else:
                dp[i][j] = dp[i-1][j]
                dp2[i][j] = dp2[i-1][j]

print(dp[-1][-1])
if dp2[-1][-1] != '':
    print(dp2[-1][-1])