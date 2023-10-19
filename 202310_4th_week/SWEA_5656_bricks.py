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

    return visited


def arrangement(disorder):
    new_order = [[0] * W for _ in range(H)]
    for i in range(W):
        bricks = []
        for j in range(H-1, -1, -1):
            if disorder[j][i] != 0:
                bricks.append(disorder[j][i])
        tmp = H - 1
        for brick in bricks:
            new_order[tmp][i] = brick
            tmp -= 1
    return new_order


def permutations(cnt):
    global min_bricks
    if cnt == N:
        check_arr = copy.deepcopy(arr)
        for j in path:
            h = 0
            while True:
                if h == H:
                    break
                if check_arr[h][j]:
                    break
                h += 1
            if h == H:
                continue
            visited_arr = BFS(h, j, check_arr[h][j])
            # 배열 돌면서 벽돌 없애기
            for n in range(H):
                for m in range(W):
                    if visited_arr[n][m]:
                        check_arr[n][m] = 0
            # 벽돌 정리
            check_arr = arrangement(check_arr)

        cnt_bricks = 0
        for a in range(H):
            for b in range(W):
                if check_arr[a][b]:
                    cnt_bricks += 1
        min_bricks = min(min_bricks, cnt_bricks)
        return

    for i in nums:
        path[cnt] = i
        permutations(cnt + 1)
        path[cnt] = -1


T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    path = [-1] * N
    nums = list(range(W))
    min_bricks = float('inf')
    permutations(0)
    print(min_bricks)
