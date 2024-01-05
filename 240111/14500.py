N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
max_point = 0

def dfs_right(y, x, sero, garo, level, point):
    global max_point
    point += arr[y][x]

    if level == 3:
        max_point = max(max_point, point)
        return
    
    if sero == 2:
        if 0 <= x - 1:
            max_point = max(max_point, point + arr[y - 1][x - 1])
        if x + 1 < M:
            max_point = max(max_point, point + arr[y - 1][x + 1])

    if garo == 2:
        if 0 <= y - 1:
            max_point = max(max_point, point + arr[y - 1][x - 1])
        if y + 1 < N:
            max_point = max(max_point, point + arr[y + 1][x - 1])

    elif garo == 1 and sero == 0:
        if y + 1 < N:
            max_point = max(max_point, point + arr[y + 1][x - 1] + arr[y + 1][x])
    
    if y + 1 < N:
        dfs_right(y + 1, x, sero + 1, garo, level + 1, point)

    if x + 1 < M:
        dfs_right(y, x + 1, sero, garo +1, level + 1, point)

def dfs_left(y, x, level, point):
    global max_point
    point += arr[y][x]

    if level == 3:
        max_point = max(max_point, point)
        return
    
    if y + 1 < N:
        dfs_left(y + 1, x, level + 1, point)

    if 0 <= x - 1:
        dfs_left(y, x - 1, level + 1, point)

for i in range(N):
    for j in range(M):
        dfs_right(i, j, 0, 0, 0, 0)
        dfs_left(i, j, 0, 0)
        
print(max_point)