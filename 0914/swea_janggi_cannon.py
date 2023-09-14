def game(i, j, move, lst):
    if move == 3:
        return
    start_y, start_x = i, j
    while 0 <= i - 1:
        i -= 1
        if arr[i][j] == 1 and (i, j) not in lst:
            while 0 <= i - 1:
                i -= 1
                if arr[i][j] == 1 and (i, j) not in lst:
                    lst.append((i, j))
                    visited[i][j] = 1
                    game(i, j, move + 1, lst)
                    lst.pop()
                    break
                else:
                    game(i, j, move + 1, lst)
            break
    i, j = start_y, start_x
    while i + 1 < N:
        i += 1
        if arr[i][j] == 1 and (i, j) not in lst:
            while i + 1 < N:
                i += 1
                if arr[i][j] == 1 and (i, j) not in lst:
                    lst.append((i, j))
                    visited[i][j] = 1
                    game(i, j, move + 1, lst)
                    lst.pop()
                    break
                else:
                    game(i, j, move + 1, lst)
            break
    i, j = start_y, start_x
    while 0 <= j - 1:
        j -= 1
        if arr[i][j] == 1 and (i, j) not in lst:
            while 0 <= j - 1:
                j -= 1
                if arr[i][j] == 1 and (i, j) not in lst:
                    lst.append((i, j))
                    visited[i][j] = 1
                    game(i, j, move + 1, lst)
                    lst.pop()
                    break
                else:
                    game(i, j, move + 1, lst)
            break
    i, j = start_y, start_x
    while j + 1 < N:
        j += 1
        if arr[i][j] == 1 and (i, j) not in lst:
            while j + 1 < N:
                j += 1
                if arr[i][j] == 1 and (i, j) not in lst:
                    lst.append((i, j))
                    visited[i][j] = 1
                    game(i, j, move + 1, lst)
                    lst.pop()
                    break
                else:
                    game(i, j, move + 1, lst)
            break


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []
    sy = sx = 0
    for n1 in range(N):
        lst = list(map(int, input().split()))
        for n2 in range(N):
            if lst[n2] == 2:
                sy, sx = n1, n2
                lst[n2] = 0
        arr.append(lst)
    cnt = 0
    visited = [[0] * N for _ in range(N)]
    game(sy, sx, 0, [])
    for y in range(N):
        for x in range(N):
            if visited[y][x]:
                cnt += 1
    print(f'#{tc}', cnt)
