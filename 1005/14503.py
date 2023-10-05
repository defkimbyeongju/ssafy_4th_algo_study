N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
cnt = 0
while True:
    around = [
        arr[r + dy[0]][c + dx[0]],
        arr[r + dy[1]][c + dx[1]],
        arr[r + dy[2]][c + dx[2]],
        arr[r + dy[3]][c + dx[3]]
    ]
    if arr[r][c] == 0:
        arr[r][c] = 2
        cnt += 1
    if 0 not in around:
        back = (d + 2) % 4
        if around[back] == 2:
            r += dy[back]
            c += dx[back]
            continue
        else:
            break
    else:
        d = (d + 3) % 4
        while around[d] != 0:
            d = (d + 3) % 4
        r += dy[d]
        c += dx[d]
print(cnt)
