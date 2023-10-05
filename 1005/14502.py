from collections import deque


def bfs():
    q = deque()
    for location in virus_list:
        q.append(location)
    cnt = 0
    visited = [[0] * M for _ in range(N)]
    while q:
        y, x = q.popleft()
        for ny, nx in [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]:
            if 0 <= ny < N and 0 <= nx < M:
                if arr[ny][nx] == 0 and not visited[ny][nx]:
                    q.append((ny, nx))
                    visited[ny][nx] = 1
                    cnt += 1
    return cnt


def f(level):
    global max_safe
    if level == 3:
        virus = bfs()
        safe = blank_first - virus
        max_safe = max(max_safe, safe)
        return
    for y, x in blank_list:
        if arr[y][x] == 0:
            arr[y][x] = 1
            f(level + 1)
            arr[y][x] = 0


N, M = map(int, input().split())
arr = []
blank_list = []
virus_list = []
blank_first = 0
for i in range(N):
    row = list(map(int, input().split()))
    arr.append(row)
    for j in range(M):
        if row[j] == 0:
            blank_list.append((i, j))
            blank_first += 1
        elif row[j] == 2:
            virus_list.append((i, j))
max_safe = 0
f(0)
print(max_safe - 3)
