turncnt = [  # [좌상, 우상, 좌하, 우하]
    [3, 1, 3, 2],  # 상 0 (현재 보고 있는 방향)
    [2, 3, 1, 3],  # 하 1
    [1, 2, 3, 3],  # 좌 2
    [3, 3, 2, 1]   # 우 3
]
nextdir = [  # [좌상, 우상, 좌하, 우하]
    [2, 3, 2, 1],  # 상 0
    [0, 3, 2, 3],  # 하 1
    [0, 3, 1, 1],  # 좌 2
    [0, 0, 2, 1]   # 우 3
]
T = int(input())
for tc in range(1, T+1):
    # reset
    apples = []
    MAP = []
    # input
    N = int(input())
    for i in range(N):
        row = list(map(int, input().split()))
        MAP.append(row)
        # 사과의 위치 찾기
        for j in range(len(row)):
            col = row[j]
            if col > 0:
                apples.append((col, i, j))  # apple : (num, y, x)
    # solve
    apples.sort()  # 먹어야 하는 사과의 순서대로 정렬

    ans = 1  # 1번 사과를 먹는다 (1개의 사과를 먹었다)
    # ** 제한 조건에 따라 테두리에는 사과가 존재하지 않는다.
    # 즉, 무조건 (0,0)에서 시작하는 특성상, 1번 사과는 무조건 [오른쪽 아래] 에 존재할 수 밖에 없다.
    # 그렇기 때문에, [1번 사과의 위치] 에서 [아래 방향] 을 본 상태로 시작하면 된다.
    dir = 1  # 현재 방향 = 아래

    # 현재 위치 = 첫번째 사과의 위치
    y = apples[0][1]
    x = apples[0][2]
    for i in range(1, len(apples)):
        ny = apples[i][1]
        nx = apples[i][2]
        # 다음 사과는 어떤 방향으로 가야 하는가?
        # 더 위에 있고, 더 왼쪽에 있고 (좌상)
        if ny < y and nx < x:
            ans += turncnt[dir][0]  # 현재 방햐에서 좌상의 방향으로 돌아야 하는 횟수 누적
            dir = nextdir[dir][0]  # 현재 방향에서 좌상의 방향으로 방향 변경
        # 더 위에 있고, 더 오른쪽에 있고 (우상)
        if ny < y and nx > x:
            ans += turncnt[dir][1]
            dir = nextdir[dir][1]
            # 더 아래에 있고, 더 왼쪽에 있고 (좌하)
        if ny > y and nx < x:
            ans += turncnt[dir][2]
            dir = nextdir[dir][2]
        # 더 아래에 있고, 더 오른쪽에 있고 (우하)
        if ny > y and nx > x:
            ans += turncnt[dir][3]
            dir = nextdir[dir][3]

        # 플레이어의 위치 이동
        y = ny
        x = nx

    # output
    print(f"#{tc} {ans}")
