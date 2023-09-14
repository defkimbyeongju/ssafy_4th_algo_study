N = int(input())
dp = [0]*(N+1)
stack = []
for i in range(1,N+1):
    min_v = 10000
    if i**0.5 == int(i**0.5):
        stack.append(i)
        dp[i] = 1
    elif i/2 in stack:
        dp[i] = 2
    else:
        for k in range(len(stack)//2+1):
            tmp = dp[i-stack[-k]]+dp[stack[-k]]
            if tmp < min_v:
                min_v = tmp
        dp[i] = min_v

print(dp[N])
