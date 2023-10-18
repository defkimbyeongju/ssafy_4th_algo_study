import copy
from collections import deque

def BFS(sy, sx, sp):
    visited = [[0] * W for _ in range(H)]
    Q = deque()
    Q.append((sy, sx, sp))
    visited[sy][sx] = 1
    while Q:
        ny, nx, np = Q.popleft()

        for dy, dx in directions:
            for p in range(np):
                new_y, new_x = ny + dy * p, nx + dx * p
                # 범위 밖이면 pass
                if 0 > new_y or 0 > new_x or new_y >= H or new_x >= W:
                    continue

                new_p = arr[new_y][new_x]
                # 빈 칸이면 pass
                if new_p == 0:
                    continue
                # 이미 방문했으면 pass
                if visited[new_y][new_x]:
                    continue

                Q.append((new_y, new_x, new_p))
                visited[new_y][new_x] = 1





def permutations(cnt):
    if cnt == N:
        check_arr = copy.deepcopy(arr)
        # path 에 순열정보 담김
        # BFS, 정렬 함수 들어갈 예정
        return check_arr

    for i in nums:
        path[cnt] = i
        permutations(cnt + 1)
        path[cnt] = -1


T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    directions= [(1, 0), (0, 1), (-1, 0), (0, -1)]
    path = [-1] * N
    nums = list(range(W))
    permutations(0)
