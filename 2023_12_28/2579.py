a = int(input())

score = [int(input()) for _ in range(a)]

dp = [0] * (a+1)

if a == 1:
    dp[1] = score[0]
elif a >= 2:
    dp[1], dp[2] = score[0], score[0]+score[1]

for i in range(3, a+1):
    dp[i] = max(dp[i-2] + score[i-1], dp[i-3] + score[i-1] + score[i-2])

print(dp[-1])