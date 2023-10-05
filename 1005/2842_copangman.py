from collections import deque
def bfs(high, low):
    global ans
    q = deque()
    q.append(P)
    visited = [[0] * N for _ in range(N)]
    visited[P[0]][P[1]] = 1
    if village[P[0]][P[1]] > high or village[P[0]][P[1]] < low:
        return False
    while q:
        y, x = q.popleft()
        for dy, dx in move:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                if low <= village[ny][nx] <= high:
                    q.append((ny, nx))
                    visited[ny][nx] = 1
    for p, q in K:
        if not visited[p][q]:
            return False
    else:
        ans = min(ans, high - low)
        return True


N = int(input())
K = []
for i in range(N):
    row = input()
    for j in range(N):
        if row[j] == 'P':
            P = (i, j)
        elif row[j] == 'K':
            K.append((i, j))
village = []
height = set()
for _ in range(N):
    row = list(map(int, input().split()))
    village.append(row)
    for n in row:
        height.add(n)
height = list(height)
height.sort()
H = len(height)
move = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
top = 0
bottom = 0
ans = 9e9
while bottom <= top < H:
    if bfs(height[top], height[bottom]):
        bottom += 1
    else:
        top += 1
print(ans)
