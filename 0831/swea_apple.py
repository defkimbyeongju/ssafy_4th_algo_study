T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 방향 [우: 1, 하: 2, 좌: 3, 상: 4]
    # 초기조건(현재위치: (0, 0), 방향: 우)
    x = y = 0
    cnt = 0
    direct = 1
    # 사과 번호 조건: 1 <= M <= 10
    for n in range(1, 11):
        for i in range(N):
            for j in range(N):
                # 사과 발견
                if arr[i][j] == n:
                    # 1사분면
                    if i < x and j > y:
                        if direct == 1:
                            cnt += 3
                            direct = 4
                        elif direct == 2:
                            cnt += 3
                            direct = 1
                        elif direct == 3:
                            cnt += 2
                            direct = 1
                        elif direct == 4:
                            cnt += 1
                            direct = 1
                    # 2사분면
                    elif i > x and j > y:
                        if direct == 1:
                            cnt += 1
                            direct = 2
                        elif direct == 2:
                            cnt += 3
                            direct = 1
                        elif direct == 3:
                            cnt += 3
                            direct = 2
                        elif direct == 4:
                            cnt += 2
                            direct = 2
                    # 3사분면
                    elif i > x and j < y:
                        if direct == 1:
                            cnt += 2
                            direct = 3
                        elif direct == 2:
                            cnt += 1
                            direct = 3
                        elif direct == 3:
                            cnt += 3
                            direct = 2
                        elif direct == 4:
                            cnt += 3
                            direct = 3
                    # 4사분면
                    elif i < x and j < y:
                        if direct == 1:
                            cnt += 3
                            direct = 4
                        elif direct == 2:
                            cnt += 2
                            direct = 4
                        elif direct == 3:
                            cnt += 1
                            direct = 4
                        elif direct == 4:
                            cnt += 3
                            direct = 3
                    # 위치 변경
                    x, y = i, j

    print(f'#{tc}', cnt)
