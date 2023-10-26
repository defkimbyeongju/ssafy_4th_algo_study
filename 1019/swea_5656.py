from collections import deque
import copy


def brick(lst):
    arr2 = copy.deepcopy(arr)
    for v in range(N):
        w = lst[v]
        h = 0
        while h < H and not arr2[h][w]:
            h += 1
        if h == H:
            continue
        q = deque()
        q.append((h, w, arr2[h][w]))
        arr2[h][w] = 0
        while q:
            y, x, power = q.popleft()
            for k in range(1, power):
                for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ny, nx = y + dy * k, x + dx * k
                    if 0 <= ny < H and 0 <= nx < W:
                        if arr2[ny][nx]:
                            q.append((ny, nx, arr2[ny][nx]))
                            arr2[ny][nx] = 0
        if v < N - 1:
            for j in range(W):
                bricks = []
                for i in range(H):
                    remain = arr2[i][j]
                    if remain:
                        bricks.append(remain)
                cnt = len(bricks)
                for i in range(cnt):
                    arr2[H - cnt + i][j] = bricks[i]
                for i in range(H - cnt):
                    arr2[i][j] = 0
    number = 0
    for i in range(H):
        for j in range(W):
            if arr2[i][j]:
                number += 1
    return number


def make_combination(level, combination):
    global min_bricks
    if level == N:
        num = brick(combination)
        min_bricks = min(min_bricks, num)
    else:
        for n in range(W):
            combination.append(n)
            make_combination(level+1, combination)
            combination.pop()


T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    min_bricks = 12 * 15
    make_combination(0, [])
    print(f'#{tc}', min_bricks)