N = int(input())
stairs = []
for _ in range(N):
    stair = int(input())
    stairs.append(stair)
# 계단이 2개 이하이면, 모두 지날 수 있기 때문에 합계를 출력
if N <= 2:
    print(sum(stairs))
# 계단이 3개 이상일 때, dp를 활용해서 문제 풀이
else:
    dp = [0] * N
    dp[0] = stairs[0]
    dp[1] = dp[0] + stairs[1]
    for i in range(2,N):
        dp[i] = max(dp[i-3]+stairs[i-1]+stairs[i], dp[i-2]+stairs[i]) # 각 i번째 계단이 마지막이라고 할 때, 나올 수 있는 최대값을 계속 구해나가는 방식
    print(dp[N-1])