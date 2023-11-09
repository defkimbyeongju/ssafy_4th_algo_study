import sys
sys.stdin= open('1.txt')
from collections import deque
import copy

def isboard(x, y):
    if 0<=x<L and 0<=y<L:
        return True
    return False

#이동 전 위치 비워주는 함수

# i번째 기사를 d의 방향으로 움직였을 때
def move(now_knight, d, arr):
    #만약 이동하려는 위치에 다른 기사가 있다면 
    # 그 기사도 함께 연쇄적으로 한 칸 밀려나게 됩니다. 
    # 그 옆에 또 기사가 있다면 연쇄적으로 한 칸씩 밀리게 됩니다. 
    # 하지만 만약 기사가 이동하려는 방향의 끝에 벽이 있다면 
    # 모든 기사는 이동할 수 없게 됩니다.
    dx, dy = dir[d]
    new_arr = [[0] * L for _ in range(L)]
    passed = deque([])
    moved = []
    i, r, c, h, w = knight_position[now_knight]
    for col in range(r, r + h):
        for row in range(c, c + w):
            nx, ny = col + dx, row + dy
            if not isboard(nx, ny) or MAP[nx][ny] == 2:
                return arr
            else:
                new_arr[nx][ny] = i
                if arr[nx][ny] != now_knight and arr[nx][ny] != 0:
                    passed.append(arr[nx][ny])
                    moved.append(arr[nx][ny])

    while passed:
        nowmove = passed.popleft()
        i, r, c, h, w = knight_position[nowmove]
        for col in range(r, r + h):
            for row in range(c, c + w):
                nx, ny = col + dx, row + dy # 한 칸 이동한 자리
                # 벽이라면 이동할 수 없다 => 바로 안된다고 하고 -1 return
                if not isboard(nx, ny) or MAP[nx][ny] ==2 :
                    return arr

                new_arr[nx][ny] = i
                if arr[nx][ny] not in moved and arr[nx][ny] != 0:
                    passed.append(arr[nx][ny]) # 그럼 그 애 추가 => 걔도 이동시켜봐야됨(연쇄 확인)
                    moved.append(arr[nx][ny]) # 움직인 애들 기억하려고
    
    if len(moved) == 0:
        return arr
    
    # 움직인 친구들 대상, 새롭게 움직인 자리에 지뢰가 몇 개 있는지 확인
    moved = set(moved)
    for i in range(1, N+1):
        if i in moved: 
            idx, r, c, h, w = knight_position[i]
            knight_position[i] = (idx, r + dx, c + dy, h, w) # 이동한 애들은 좌표 바꿔줌
            idx, r, c, h, w = knight_position[i]
            for col in range(r, r + h):
                for row in range(c, c + w):
                    if isboard(col, row):
                        if MAP[col][row] == 1:
                            full, damage = knight_energy[i]
                            if full - (damage + 1) == 0:
                                dead.append(i) # 죽은 기사 저장
                            knight_energy[i] = (full, damage + 1)

    # 여기까지 왔으면 new_arr 에 이동한 기사 + 연쇄적으로 이동한 기사들의 위치 표시됨
    # 움직이지 않은 친구들도 표시해주기
    for i in range(1, N+1):
        if i != now_knight and i not in moved and i not in dead: # 본인이 아니고 움직인 적이 없는 기사라면,
            idx, r, c, h, w = knight_position[i]
            for col in range(r, r + h):
                for row in range(c, c + w):
                    if isboard(col, row):
                        new_arr[col][row] = idx
    
    # 그럼 arr에는 한 턴 전, new_arr 는 한 턴 후가 됨
    arr = copy.deepcopy(new_arr)
    return arr
                    

# 최종 : 생존한 기사들이 총 받은 데미지의 합
L, N, Q = map(int, input().split()) # 체스크기, 기사 정보수, 왕 명령 수
MAP = [list(map(int, input().split())) for _ in range(L)] # 함정, 벽 정보가 담겨있는 맵

arr = [[0] * L for _ in range(L)] # 기사들의 영역 상태를 표시하기 위한 배열
knight_position = [(-1, -1), ]
knight_energy = [(-1, -1), ]
dead = []

### 기사들 정보 입력 받기
for i in range(1, N+1): #  입력은 1번 기사부터 N번 기사까지 순서대로 주어짐
    r, c, h, w, k = map(int, input().split()) # 처음위치 r, c, 세로, 가로, 초기 체력
    knight_position.append((i, r - 1, c - 1, h, w)) # 처음 위치가 (1, 1)로 가정하므로 1씩 빼준다
    knight_energy.append((k, 0)) # 체력, 입은 대미지
    for col in range(r -1, r -1 + h):
        for row in range(c - 1, c - 1 + w):
            arr[col][row] = i # arr에 해당 기사가 차지하는 부분 표시(2번 기사 - 2로 표시)

dir = {0 : (-1, 0), 1 : (0, 1), 2 : (1, 0), 3 : (0, -1)} # 위, 오른쪽, 아래쪽, 왼쪽
### 왕 명령 입력 받기
for turn in range(Q):
    i, d = map(int, input().split()) # i번 기사에서 d로 한 칸 이동하라는 의미
    if i not in dead: # 죽은 기사가 아닌 경우 움직일 수 있음
        arr = move(i, d, arr)


res = 0
for i in range(1, N+1):
    if i not in dead:
        full, damage = knight_energy[i]
        # print(i, full, damage)
        if full - damage > 0:
            res += damage

print(res)