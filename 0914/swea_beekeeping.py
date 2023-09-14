def dfs(four):
    global max_hap
    if len(four) == 4:
        hap = 0
        for p, q in four:
            hap += arr[p][q]
        max_hap = max(max_hap, hap)
        return
    (y, x) = four[-1]
    if x % 2:
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1), (1, -1), (1, 1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and (ny, nx) not in four:
                four.append((ny, nx))
                dfs(four)
                four.pop()
    else:
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (-1, -1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M and (ny, nx) not in four:
                four.append((ny, nx))
                dfs(four)
                four.pop()


def ys(y, x):
    global max_hap
    if x % 2:
        hap1 = 0
        for ny, nx in [(y, x), (y, x-1), (y, x+1), (y+1, x)]:
            if 0 <= ny < N and 0 <= nx < M:
                hap1 += arr[ny][nx]
        hap2 = 0
        for ny, nx in [(y, x), (y+1, x-1), (y+1, x+1), (y-1, x)]:
            if 0 <= ny < N and 0 <= nx < M:
                hap2 += arr[ny][nx]
        max_hap = max(max_hap, hap1, hap2)
    else:
        hap1 = 0
        for ny, nx in [(y, x), (y, x - 1), (y, x + 1), (y - 1, x)]:
            if 0 <= ny < N and 0 <= nx < M:
                hap1 += arr[ny][nx]
        hap2 = 0
        for ny, nx in [(y, x), (y - 1, x + 1), (y - 1, x - 1), (y + 1, x)]:
            if 0 <= ny < N and 0 <= nx < M:
                hap2 += arr[ny][nx]
        max_hap = max(max_hap, hap1, hap2)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_hap = 0
    for i in range(N):
        for j in range(M):
            dfs([(i, j)])
            ys(i, j)
    print(f'#{tc}', max_hap)
