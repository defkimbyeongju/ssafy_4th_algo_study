from collections import deque
n,k = map(int, input().split())
dp = [[float('inf'),0] for _ in range(200004)] # 21e3 -> float('inf')로 바꾸니 정답 처리됨. 초기값 설정 잘 봐야됨
dp[n][0] = 0
dp[n][1] = 1
def bfs(start):
    q = deque()
    q.append(start)
    while q:
        now = q.popleft()
        go = [now-1, now+1, now*2]
        if 0 < now < k:
            for i in range(3):
                if dp[go[i]][0] > dp[now][0]+1:
                    dp[go[i]][0] = dp[now][0]+1
                    dp[go[i]][1] = 1
                    q.append(go[i])
                elif dp[go[i]][0] == dp[now][0]+1:
                    dp[go[i]][1] += 1
                    q.append(go[i])
        elif now > k: # k보다 큰 경우는 -1만 하기
            if dp[now-1][0] > dp[now][0]+1:
                dp[now-1][0] = dp[now][0]+1
                dp[now-1][1] = 1
                q.append(now-1)
            elif dp[now-1][0] == dp[now][0]+1:
                dp[now-1][1] += 1
                q.append(now - 1)
        elif now == 0:
            if dp[now+1][0] > dp[now][0]+1:
                dp[now+1][0] = dp[now][0]+1
                dp[now+1][1] = 1
                q.append(now+1)
            elif dp[now+1][0] == dp[now][0]+1:
                dp[now+1][1] += 1
                q.append(now+1)
bfs(n)
print(dp[k][0])
print(dp[k][1])