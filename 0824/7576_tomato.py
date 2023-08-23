from collections import deque
M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
check = True
Q = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            Q.append((i, j, 0))
        elif arr[i][j] == 0:
            check = False
while Q:
    y, x, d = Q.popleft()
    ans = d
    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < M:
            if arr[ny][nx] == 0:
                Q.append((ny, nx, d+1))
                arr[ny][nx] = 1
no = False
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            no = True
if no:
    print(-1)
elif check:
    print(0)
else:
    print(d)
