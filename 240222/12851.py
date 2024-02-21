from collections import deque
N, K = map(int, input().split())
visited = [0] * 100001
q = deque()
q.append((N, 0))
cnt = 0
ans = 100000
while q:
    t, s = q.popleft()
    visited[t] = 1
    if t == K and not cnt:
        cnt += 1
        ans = s
    elif t == K and s == ans:
        cnt += 1
    elif s > ans:
        break
    for i in [t-1, t+1, 2 * t]:
        if 0 <= i <= 100000 and not visited[i]:
            q.append((i, s + 1))
print(ans)
print(cnt)
