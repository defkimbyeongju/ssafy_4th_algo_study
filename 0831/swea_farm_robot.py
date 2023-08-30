move = [
    [(0, 1, 3), (-1, 0, 0), (-1, 0, 2), (1, 0, 1)],  # 상
    [(0, -1, 2), (1, 0, 1), (0, 1, 3), (-1, 0, 0)],  # 하
    [(-1, 0, 0), (0, -1, 2), (1, 0, 1), (0, 1, 3)],  # 좌
    [(1, 0, 1), (0, 1, 3), (0, -1, 0), (0, -1, 2)]   # 우
]


def robot(y, x, dir, day):
    if arr[y][x] == 0:
        for dy, dx, d in move[dir]:
            ny, nx = y + dy, x + dx
            if arr[ny][nx] % 100 == 0:
                arr[y][x] = 10
                robot(ny, nx, d, day+1)
                break
        else:
            robot(y, x, dir, day+1)
    elif arr[y][x] == 100:
        cnt += 1
        K[y][x] += 1
        arr[y][x] = 0


def crop():
    for i in range(1, N-1):
        for j in range(1, N-1):
            if 10 <= arr[i][j] < 100:
                arr[i][j] += 1


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    K = [[1] * N for _ in range(N)]
