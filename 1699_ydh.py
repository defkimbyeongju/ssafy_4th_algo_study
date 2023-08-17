def min_squares(n):
    # dp[i]는 최소 항 개수를 저장
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        # 최악의 경우는 모두 1^2로 구성된 경우이므로 i로 초기화
        dp[i] = i
        
        j = 1
        while j * j <= i:
            # i보다 작거나 같은 제곱수 j^2를 사용하여 i를 만듬
            dp[i] = min(dp[i], 1 + dp[i - j*j])
            j += 1
    
    return dp[n]


n = int(input())
result = min_squares(n)
print(result)
