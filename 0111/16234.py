import copy
N, L, R = map(int, input().split())
from collections import deque
arr = [list(map(int, input().split())) for _ in range(N)]
dir = [(0,1),(1,0),(-1,0),(0,-1)]
result = 0
def bfs(row,col):
    count = 0
    total = 0
    change = []
    q = deque()
    q.append((row,col))
    used[row][col] = 1
    while q:
        i,j = q.popleft()
        change.append([i,j])
        count += 1
        total += arr[i][j]
        for y,x in dir:
            ny,nx = i+y, j+x
            if 0<=ny<N and 0<=nx<N and not used[ny][nx]:
                diff = abs(arr[i][j] - arr[ny][nx])
                if L<=diff<=R:
                    used[ny][nx] = 1
                    q.append((ny,nx))
    new_value = total // count
    for i,j in change:
        arr[i][j] = new_value

while True:
    prev = copy.deepcopy(arr)
    used = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not used[i][j]:
                bfs(i,j)
    if prev == arr:
        break
    result += 1
print(result)
