from collections import deque

M, N = map(int, input().split())    # 토마토 보관 창고 입력받기
arr = [list(map(int, input().split())) for _ in range(N)]
direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # 토마토 후숙 방향 설정
Q = deque()      # Q 생성
visited = [[0] * M for _ in range(N)]   # visited 생성
# 시작 토마토 찾기
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            Q.append((i, j))    # enQ

while Q:    # 큐가 비어있지 않는 한
    y, x = Q.popleft()     # deQ
    for dy, dx in direction:    # 해당 토마토 상,하,좌,우 에 대해
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < M and not arr[ny][nx]: # 창고 범위 안, 후숙되지 않은 토마토
            Q.append((ny, nx))  # enQ
            arr[ny][nx] = 1     # 후숙되었음을 표시
            visited[ny][nx] = visited[y][x] + 1     # visited 에 day 값을 저장


def check():    # 후숙완료 된 토마토 창고를 검사하는 함수
    day = 0     # 며칠 걸렸는 지 저장할 변수
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:  # 후숙되지 않은 토마토 발견 시,
                return -1       # -1 리턴
            if visited[i][j] > day:     # visited 순회하며
                day = visited[i][j]     # 가장 오래 걸린 토마토 day를 찾기
    return day  # day 리턴


print(check())  # 결과 출력
