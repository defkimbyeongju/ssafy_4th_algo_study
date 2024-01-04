from collections import deque
import heapq

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

# 상어의 초기 위치와 상태
for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            shark = [i, j, 2, 0] 
            board[i][j] = 0

# shark[0]: 상어의 현재 x좌표 (행)
# shark[1]: 상어의 현재 y좌표 (열)
# shark[2]: 상어의 현재 크기
# shark[3]: 상어가 현재 크기에서 먹은 물고기의 수

def bfs(shark):
    visited = [[False] * N for _ in range(N)]
    queue = deque([(shark[0], shark[1], 0)]) 
    fishes = []                                 # 먹을 수 있는 물고기의 리스트
    visited[shark[0]][shark[1]] = True

    while queue:
        x, y, dist = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if board[nx][ny] > 0 and board[nx][ny] < shark[2]:
                    heapq.heappush(fishes, (dist+1, nx, ny))    # 먹을 수 있는 물고기를 찾으면 리스트에 추가
                if board[nx][ny] <= shark[2]:                   # 이동 가능한 위치로 이동
                    visited[nx][ny] = True
                    queue.append((nx, ny, dist+1))

    if fishes:
        return fishes[0]  # 먹을 수 있는 물고기 중 가장 가까운 물고기
    else:
        return None

time = 0
while True:
    result = bfs(shark)
    if not result:
        break               # 먹을 수 있는 물고기가 없다면 종료

    dist, nx, ny = result
    board[nx][ny] = 0       # 물고기를 먹고 빈 칸으로
    time += dist            # 시간 추가
    shark[0], shark[1] = nx, ny     # 상어 위치 변경
    shark[3] += 1                   # 먹은 물고기 수 증가

    if shark[2] == shark[3]:    # 먹은 물고기 수가 상어의 크기와 같다면
        shark[2] += 1           # 상어 크기 증가
        shark[3] = 0            # 먹은 물고기 수 초기화

print(time) 
