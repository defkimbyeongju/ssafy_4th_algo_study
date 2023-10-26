def solution(money):
    N = len(money)
    dp1 = [0] * (N)
    dp1[0] = money[0]
    dp1[1] = max(money[:2])
    for k in range(2, N-1):
        dp1[k] = max(dp1[k-2] + money[k], dp1[k-1])
    dp2 = [0] * (N)
    dp2[0] = money[1]
    dp2[1] = max(money[1:3])
    for k in range(2, N-1):
        dp2[k] = max(dp2[k-2] + money[k+1], dp2[k-1])
    return max(max(dp1), max(dp2))