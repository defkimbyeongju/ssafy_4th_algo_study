def nemo(q, p, d, lst):
    # d = 방향, {0: 우하향, 1: 좌하향, 2: 좌상향, 3: 우상향}
    # lst = 지금까지 지나온 디저트의 종류
    global max_cnt
    if d == 0 or d == 1 or d == 2:
        # 현재 방향 그대로 이동
        nq1, np1 = q + move[d][0], p + move[d][1]
        # 사각형은 무조건 아래로만 만들 것이므로 행은 시작 지점보다 밑에만
        # 디저트 종류도 중복되면 안 됨
        if start_y < nq1 < N and 0 <= np1 < N and arr[nq1][np1] not in lst:
            lst.append(arr[nq1][np1])
            nemo(nq1, np1, d, lst)
            lst.pop()
        # 다음 방향으로 이동(꺾기)
        nq2, np2 = q + move[d+1][0], p + move[d+1][1]
        # d == 2 인 경우에만 해당
        # 꺾었는데 시작위치 == 정답 갱신하고 return
        if nq2 == start_y and np2 == start_x:
            max_cnt = max(max_cnt, len(lst))
            return
        if start_y < nq2 < N and 0 <= np2 < N and arr[nq2][np2] not in lst:
            lst.append(arr[nq2][np2])
            nemo(nq2, np2, d+1, lst)
            lst.pop()
    elif d == 3:
        # 위와 같음
        nq, np = q + move[d][0], p + move[d][1]
        if nq == start_y and np == start_x:
            max_cnt = max(max_cnt, len(lst))
            return
        if start_y < nq < N and 0 <= np < N and arr[nq][np] not in lst:
            lst.append(arr[nq][np])
            nemo(nq, np, d, lst)
            lst.pop()


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 우하향, 좌하향, 좌상향, 우상향 순으로 이동할 것임
    move = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
    max_cnt = 0
    for y in range(N - 2):  # 밑에 두 줄은 사각형 만들 수 없으므로 고려 X
        for x in range(1, N - 1):  # 양 옆에 두 줄은 사각형 만들 수 X
            start_y, start_x = y, x  # 사각형 만들기 시작하는 곳
            nemo(y, x, 0, [arr[y][x]])
    print(f'#{tc}', max_cnt if max_cnt else -1)
