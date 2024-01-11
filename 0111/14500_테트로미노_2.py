# 2번 풀이

def dfs(y, x, cnt, s):
    global ans
    if cnt == 4:
        ans = max(ans, s)
        return
    for dy, dx in dir:
        ny, nx = y+dy, x+dx
        if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] == 0:
            visited[ny][nx] = 1
            dfs(ny, nx, cnt+1, s+paper[ny][nx])
            visited[ny][nx] = 0
# ㅓㅏㅗㅜ방향을 제외하고는 dfs로 커버 가능한 모양이므로, dfs로 최대값 탐색

def rest(y, x):
    cnt = 0
    s = paper[y][x]
    global ans
    for dy, dx in dir:
        ny, nx = y+dy, x+dx
        if 0 <= ny < N and 0 <= nx < M:
            cnt += 1
            s += paper[ny][nx]
    # 가능한 방향 모두 더함
    if cnt == 4:
        for dy, dx in dir:
            ny, nx = y+dy, x+dx
            ans = max(s-paper[ny][nx], ans)
    # 4방향 모두 만족했을 때는 하나 빼서 max인 값과 비교
    else:
        ans = max(s, ans)
    # 3방향 만족했을 때는 그대로 비교 (나머지는 알아서 걸러짐)

N, M = map(int, input().split())

paper = [list(map(int, input().split())) for _ in range(N)]
dir = [(0,1),(0,-1),(1,0),(-1,0)]
visited = [[0]*M for _ in range(N)]
ans = 0
for y in range(N):
    for x in range(M):
        visited[y][x] = 1
        dfs(y,x, 1, paper[y][x])
        rest(y, x)
        visited[y][x] = 0
# dfs와 나머지를 매 위치에 대해 돌려서 최대값 산출
print(ans)


            
