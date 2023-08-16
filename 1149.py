N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# 색이 3개이므로 요소가 3개인 리스트를 N개 생성
dp = [[0, 0, 0] for _ in range(N)]
# 첫 리스트는 1번 집
dp[0] = arr[0]
for i in range(1, N):
    # 각 요소는 해당 색과 이전 집의 색이 같지 않은 경우 중 최소값
    dp[i][0] = min(arr[i][0] + dp[i - 1][1], arr[i][0] + dp[i - 1][2])
    dp[i][1] = min(arr[i][1] + dp[i - 1][0], arr[i][1] + dp[i - 1][2])
    dp[i][2] = min(arr[i][2] + dp[i - 1][0], arr[i][2] + dp[i - 1][1])
# 세가지 색 중 가장 작은 값이 정답
ans = min(dp[N - 1][0], dp[N - 1][1], dp[N - 1][2])
print(ans)
