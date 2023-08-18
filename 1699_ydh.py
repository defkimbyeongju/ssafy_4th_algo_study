def func(n):
    dp = [0] * (n + 1)  # 각 숫자별 최소 항 개수를 저장

    for i in range(1, n + 1):
        # 최대 항 개수 i로 초기화 (1의 제곱이 n개)
        dp[i] = i

        j = 1
        while j * j <= i:
            # i보다 작거나 같은 제곱수 j^2를 사용하여 i를 만듬
            dp[i] = min(dp[i], 1 + dp[i - j * j])
            j += 1

    return dp[n]


N = int(input())
print(func(N))
