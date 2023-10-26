# 백준 7576 토마토
def bfs(queue): # bfs로 문제 해결. 시간 초과가 나와서 deque도 써보고 했지만, 안돼서 결국 pypy로 제출
    dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while queue:
        i, j = queue.popleft() # 토마토가 있는 좌표 값을 큐에서 꺼내기
        for y, x in dir:
            ny, nx = y+i, x+j
            if 0<=ny<N and 0<=nx<M: # 방향배열 처리
                if arr[ny][nx] == 0: # 인근에 익지 않은 토마토가 있을 때
                    arr[ny][nx] = 1
                    visited[ny][nx] = visited[i][j] + 1 # 이전 visited 값에 1을 더한 값을 저장해주면서 동시에 다른 위치에서 토마토를 익혀줌
                    queue.append((ny,nx))

from collections import deque
M,N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
queue = deque()
visited = [[0]*M for _ in range(N)]

if 0 not in sum(arr, []): # 처음부터 모든 토마토가 다 익었을 때
    result = 0
else:
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                queue.append((i,j))  # 익은 토마토가 있는 지점은 큐에 저장하고 방문처리
                visited[i][j] = 1
    bfs(queue) # bfs 돌려주기
    if 0 in sum(arr,[]): # 아직도 익지 않은 토마토가 남아있으면 -1을 출력
        result = -1
    else:
        result = max(sum(visited, []))-1 # visited에서 가장 높은 값을 출력

print(result)
