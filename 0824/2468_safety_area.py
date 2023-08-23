from collections import deque

N = int(input())
area = []
max_h = 0
for i in range(N):
    area.append(list(map(int, input().split())))
    max_h = max(max_h, max(area[i]))
max_cnt = 0
for rain in range(max_h):
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if area[i][j] > rain and not visited[i][j]:
                queue = deque()
                queue.append((i, j))
                visited[i][j] = 1
                while queue:
                    (it, jt) = queue.popleft()
                    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        ni, nj = it + di, jt + dj
                        if 0 <= ni < N and 0 <= nj < N:
                            if area[ni][nj] > rain and not visited[ni][nj]:
                                queue.append((ni, nj))
                                visited[ni][nj] = 1
                cnt += 1
    max_cnt = max(max_cnt, cnt)
print(max_cnt)
