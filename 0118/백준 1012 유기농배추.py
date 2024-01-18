from collections import deque
T = int(input())
dir = [(0,1),(1,0),(0,-1),(-1,0)]
def bfs(y,x):
    q = deque()
    q.append((y,x))
    while q:
        i, j = q.popleft()
        for dj, di in dir:
            ny, nx = i+di, j+dj
            if 0<=ny<N and 0<=nx<M:
                if arr[ny][nx] == 1:
                    arr[ny][nx] = 0
                    q.append((ny,nx))
    

for _ in range(T):
    M, N, K = map(int, input().split())
    arr = [[0]*M for _ in range(N)]
    for _ in range(K):
        x,y = map(int, input().split())
        arr[y][x] = 1
    count = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                bfs(i,j)
                count += 1
    print(count)
        
