import heapq


def dijkstra():
    min_fuel = [[float('inf')] * N for _ in range(N)]
    min_fuel[0][0] = 0

    heap = [(0, 0, 0)]  # (연료 소모량, row, col)

    while heap:
        fuel, i, j = heapq.heappop(heap)

        if fuel > min_fuel[i][j]:
            continue

        for y, x in dir:
            ni, nj = i + y, j + x

            if 0 <= ni < N and 0 <= nj < N:
                height_diff = arr[ni][nj] - arr[i][j]
                new_fuel = fuel + height_diff * height_diff

                if new_fuel < min_fuel[ni][nj]:
                    min_fuel[ni][nj] = new_fuel
                    heapq.heappush(heap, (new_fuel, ni, nj))

    return min_fuel[N - 1][N - 1]


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    min_fuel = dijkstra()

    tunnels = []

    for _ in range(M):
        x1, y1, x2, y2, power = map(int, input().split())
        tunnels.append(power)

    tunnels.sort()

    for tunnel in tunnels:
        min_fuel = min(min_fuel, min_fuel + tunnel)

    print(f'#{tc} {min_fuel}')