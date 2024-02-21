# 상호작용 연쇄 이동 함수
def move(y,x,dy,dx,value):
    origin_santa = arr[y][x] # 기존 위치에 있던 산타
    arr[y][x] = value # 밀려 나온 산타가 그 자리에 자리함
    santa_loc[value-1][0], santa_loc[value-1][1] = y,x # Santa의 정보를 담은 리스트에서도 좌표 값 변경해줌
    # 기존 위치 산타가 이동할 위치
    ny = y + dy
    nx = x + dx
    if 0<=ny<N and 0<=nx<N: # 밀려난 그 위치가 범위 안에 있다면
        if arr[ny][nx] != 0: # 그 자리에도 누군가 있다면
            move(ny,nx,dy,dx,origin_santa)
        else: # 그 자리에 아무도 없다면
            arr[ny][nx] = origin_santa
            santa_loc[origin_santa - 1][0], santa_loc[origin_santa - 1][1] = ny, nx
    else: # 바깥으로 밀려나면 out 처리
        santa_loc[origin_santa-1][3] = -1

# 주요한 자료 리스트
# 1. arr -> 게임이 일어나는 board판
# 2. santa_loc -> santa의 y,x 좌표값, 획득 점수, 기절 여부를 담은 리스트
# 3. distance -> 루돌프가 이동할 때만 사용. 가장 가까운 산타의 위치를 파악하기 위함
N, M, P, C, D = map(int, input().split())
arr = [[0]*N for _ in range(N)]
Ry, Rx = map(int,input().split())
Ry -= 1
Rx -= 1
arr[Ry][Rx] = -1 # 루돌프는 -1로 표시
santa_loc = [[] for _ in range(P)] # 산타들의 좌표, 점수, 기절여부를 체크할 리스트
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 산타가 움직일 수 있는 방향
for _ in range(P):
    santa, Sy, Sx = map(int, input().split())
    santa_loc[santa-1] = [Sy-1, Sx-1, 0, 0] # y좌표, x좌표, 점수, 기절 여부(기절하면 2, 아웃이면 -1)
    arr[Sy-1][Sx-1] = santa # 산타들은 인덱스가 아닌 각자의 고유 번호로 표시
for _ in range(M):
    # 루돌프 먼저 이동
    arr[Ry][Rx] = 0 # 기존 위치 초기화
    distance = [[] for _ in range(P)]
    for i in range(P):
        if santa_loc[i][3] == -1: # 아웃인 곳은 제껴야됨
            distance[i] = [float('inf'),santa_loc[i][0],santa_loc[i][1], i]
            continue
        temp = (Ry - santa_loc[i][0]) ** 2 + (Rx - santa_loc[i][1]) ** 2
        distance[i] = [temp, santa_loc[i][0],santa_loc[i][1], i] # 거리, y좌표, x좌표, 산타 인덱스
    distance.sort(key=lambda x:(x[0], -x[1], -x[2])) # 우선 순위(거리, y좌표, x좌표)에 따라 정렬해주기
    # 좌표 차이로 다음 방향 정해주기
    dy,dx = 0,0
    if Ry > distance[0][1]:
        dy = -1
    elif Ry < distance[0][1]:
        dy = 1
    if Rx > distance[0][2]:
        dx = -1
    elif Rx < distance[0][2]:
        dx = 1
    # 루돌프 이동
    Ry += dy
    Rx += dx
    # 루돌프가 이동해서 산타 만나면 산타 튕겨져 나가기
    if Ry == distance[0][1] and Rx == distance[0][2]:
        cracked_santa = arr[Ry][Rx] # 루돌프랑 충돌한 산타 번호
        arr[Ry][Rx] = -1 # 해당 위치는 루돌프가 먹음
        ny = Ry+dy*C
        nx = Rx+dx*C
        santa_loc[distance[0][3]][2] += C # 루돌프랑 충돌했으니 해당 산타는 점수 획득
        # 범위 밖이라면 아웃 처리
        if ny >= N or ny < 0 or nx >= N or nx < 0:
            santa_loc[distance[0][3]][3] = -1
            # santa_loc[distance[0][3]] = [ny, nx, santa_loc[distance[0][3]][2], -1]
        # 범위 안에 들어오면 루돌프랑 충돌했으니 기절 처리
        else:
            # 이동한 위치에 다른 산타가 있을 경우 상호작용
            if arr[ny][nx] != 0:
                move(ny,nx,dy,dx,cracked_santa)
                santa_loc[cracked_santa-1][3] = 2 # 기절 처리
            # 이동 위치에 아무도 없으면 그 자리 먹고 산타 기절 처리 최신화
            else:
                arr[ny][nx] = cracked_santa
                santa_loc[cracked_santa-1] = [ny, nx, santa_loc[distance[0][3]][2], 2]
    # 이동한 위치에 산타가 없으면 그냥 그 자리 먹고 끝
    else:
        arr[Ry][Rx] = -1

    # P명의 산타 이동 차례
    for i in range(P):
        if santa_loc[i][3] == -1: # 아웃이면 움직이지 않음
            continue
        elif santa_loc[i][3] > 0: # 기절이면 이번 턴은 제끼고 점수는 획득
            santa_loc[i][3] -= 1
            continue
        y,x = santa_loc[i][0], santa_loc[i][1]
        dist = (Ry-y) ** 2 + (Rx-x) ** 2  # 현재 위치에서 산타와의 거리
        min_dist = dist # 최소 거리 구하기 위한 변수 설정. 기본값은 현재 위치에서 산타와의 거리
        min_idx = -1 # 최소 거리가 되는 방향의 인덱스
        # 상,우,하,좌 순서
        for idx in range(4):
            dy, dx = dir[idx][0], dir[idx][1]
            ny,nx = y+dy, x+dx
            if 0<=ny<N and 0<=nx<N and (arr[ny][nx] == 0 or arr[ny][nx] == -1): # 범위 안에 들어오고
                temp_dist = (Ry-ny) ** 2 + (Rx-nx) ** 2
                if temp_dist < min_dist: # 거리가 더 가까워지고, 해당 칸이 비어있다면
                    min_dist = min(min_dist, temp_dist)
                    min_idx = idx
        # 마땅히 갈 곳 없으면 1점 획득하고 이동 안함
        if min_idx == -1:
            santa_loc[i][2] += 1
            continue
        # 갈 방향 정하고 이동하기
        dy, dx = dir[min_idx][0], dir[min_idx][1]
        ny, nx = y+dy, x+dx
        arr[y][x] = 0 # 현 위치는 초기화
        if arr[ny][nx] == -1: # 루돌프랑 충돌한다면
            santa_loc[i][2] += D # 점수 획득
            # 튕겨져 나가는데, 방향은 반대로 바꿔줘야 함
            dy *= -1
            dx *= -1
            ny += dy*D
            nx += dx*D
            if 0<=ny<N and 0<=nx<N: # 범위 안에 들어올 때
                if arr[ny][nx] != 0: # 튕겨 나간 곳에 또 다른 산타가 있다면
                    move(ny,nx,dy,dx,i+1)
                    santa_loc[i][3] = 2 # 기절 처리
                else: # 튕겨 나간 곳이 비어 있다면 그 자리 먹기
                    arr[ny][nx] = i+1
                    santa_loc[i] = [ny,nx,santa_loc[i][2],2]
            else: # 나가리 되면
                santa_loc[i] = [ny, nx, santa_loc[i][2], -1]
        # 루돌프랑 충돌 안하면 그 자리 먹기
        else:
            arr[ny][nx] = i+1
            santa_loc[i] = [ny, nx, santa_loc[i][2], 0]

    # 매 턴이 끝나고, 남아 있는 산타는 점수 1저 획득
    for i in range(P):
        if santa_loc[i][3] != -1:
            santa_loc[i][2] += 1


for i in range(P):
    print(santa_loc[i][2], end=' ')
