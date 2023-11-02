INF = 10e7

direction = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}  # 상 하 좌 우


# 지금 지도에 있는 애들이 뭔지 알아내는 함수
def find(arr):
    newgerms = []
    for i in range(N):
        for j in range(N):
            if arr[0][i][j] > 0:
                newgerms.append([i, j, arr[0][i][j], arr[1][i][j]])

    return sorted(newgerms, key=lambda x: x[2])


# 현재 상태 germ을 입력받은 후1초 움직이고 나서 map에 배치된 모습을 return
def move(germ):
    for g in germ:
        dir = g[3]
        dx, dy = direction[dir]
        g[0] += dx
        g[1] += dy
        if g[0] == 0 or g[0] == N-1 or g[1] == 0 or g[1] == N-1:
            g[2] //= 2
            if g[3] == 1 or g[3] == 3:
                g[3] += 1
            else:
                g[3] -= 1

    new_map = [[[0] * N for _ in range(N)] for _ in range(2)]

    for g in germ:
        c, r, num, d = g[0], g[1], g[2], g[3]
        if 0<=c<N and 0<=r<N:
            new_map[1][c][r] = d
            new_map[0][c][r] += num

    return new_map


for tc in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    germ = []
    for idx in range(K):
        c, r, num, d = map(int, input().split())
        germ.append([c, r, num, d])
    germ = sorted(germ, key=lambda x: x[2])
    time = 0
    while True:

        MAP = move(germ)
        germ = find(MAP)
        time += 1

        if time == M:
            break

    print(f'#{tc} {sum(map(sum, MAP[0]))}')