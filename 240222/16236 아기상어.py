from collections import deque
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
shark = [-1,-1,2]
fishes = []
result = 0
ate = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 0:
            continue
        if arr[i][j] == 9:
            shark[0], shark[1] = i, j
            continue
        fishes.append([i,j,arr[i][j]])

# 먹을 수 있는 물고기가 여러 마리일 경우
# 우선순위1: 거리 우선순위2: 가장 위, 우선순위3: 가장 왼쪽
# 크기가 동일한 물고기는 먹지는 못하지만, 그 칸을 지나갈 수는 있음

# 해결 방법: 상어의 크기가 바뀔 때마다 먹을 수 있는 물고기 리스트를 갱신. 해당 칸으로 갈 수 있는지 확인
def distance_check(si,sj): # 아기상어의 위치에서 각 좌표에 대해 최소 거리를 반환
    used = [[float('inf')]*n for _ in range(n)]
    used[si][sj] = 0
    q = deque()
    q.append((si,sj))
    dir = [(0,1),(1,0),(0,-1),(-1,0)]
    while q:
        y,x = q.popleft()
        for i,j in dir:
            ny, nx = y+i, j+x
            if 0<=ny<n and 0<=nx<n: # 범위 안에 들어올 때
                if arr[ny][nx] <= shark[2] and used[ny][nx] > used[y][x]+1: # 아기상어가 갈 수 있는 칸이며, 거리가 더 짧아진다면
                    q.append((ny,nx))
                    used[ny][nx] = used[y][x] + 1
    return used

def priority_check(fish, used): # 우선 순위 체크
    can_go = []
    for f in fish:
        if f[2] < shark[2]:
            can_go.append(f)
    if not can_go:
        return []
    prior = []
    min_v = 21e3
    for go in can_go:
        d = used[go[0]][go[1]]
        if d < min_v:
            min_v = d
            prior.clear() # 최소값이 갱신되면 클리어
            prior.append(go+[d])
        elif d == min_v:
            prior.append(go+[d])
    # 제일 위에 있는 것 == y값이 작은 순서, 제일 왼쪽에 있는 것 == x값이 작은 순서. 우선순위 큐에 담으면 자동으로 정렬
    if prior: # 물고기 크기는 먹을 수 있지만, 주변에 큰 물고기들에 둘러 쌓여 갈 수 없는 경우가 존재함.
        prior.sort(key=lambda x: (x[0], x[1]))
        return prior[0]
    else:
        return []

while True:
    used = distance_check(shark[0], shark[1]) # 처음 아기 상어의 위치에서 각 좌표에 대한 거리 값을 반환
    p = priority_check(fishes, used) # 물고기 우선순위 반환
    if not p: # 먹을 수 있는 물고기가 없다면 엄마 상어에게 도움을 요청해야 하므로 종료
        break
    result += p[3] # 결과 값에 우선순위 물고기 거리 추가
    arr[p[0]][p[1]] = 9 # 해당 물고기 위치에 아기상어 배치
    arr[shark[0]][shark[1]] = 0 # 아기 상어가 기존에 있던 위치 지워줌
    fishes.remove([p[0],p[1],p[2]]) # fishes 배열에서도 삭제
    shark[0], shark[1] = p[0], p[1] # shark 위치 최신화
    ate += 1 # 한 마리 먹음
    if ate == shark[2]: # 만약 먹은 물고기 수가 아기상어의 크기와 동일하다면 아기상어 크기 1 증가
        shark[2] += 1
        ate = 0

print(result)