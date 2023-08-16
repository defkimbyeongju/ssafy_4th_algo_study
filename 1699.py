N = int(input())
# 초기 값은 크게
dp = [N] * (N + 1)
# N이 제곱수일 경우를 위해
dp[0] = 0
# N이 1이면 1임
dp[1] = 1
# 2부터 N까지
for i in range(2, N + 1):
    # 1부터 루트 N 이하의 가장 큰 자연수 까지
    for j in range(1, int(i ** (1/2)) + 1):
        # i에서 j의 제곱을 뺀 값 중 가장 적은 최소 개수를 가진 값을 찾는다
        check = dp[i - j ** 2]
        if dp[i] > check:
            dp[i] = check + 1
print(dp[N])
