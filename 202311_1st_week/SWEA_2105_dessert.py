def square(y, x):
    # 첫번째 점 가능한 리스트 생성하기
    first = []
    ny, nx = y + 1, x + 1
    while ny <= (N - 2) and nx <= (N - 1):
        first.append((ny, nx))
        ny += 1
        nx += 1

    # 마지막 점 가능한 리스트 생성
    last = []
    ly, lx = y + 1, x - 1
    while ly <= (N - 2) and lx >= 0:
        last.append((ly, lx))
        ly += 1
        lx -= 1

    # 첫번째 점들을 순회하기
    result = [(y, x)]
    max_v = -1

    for fy, fx in first:
        # 두번째 점 가능한 리스트 생성
        second = []
        sy, sx = fy + 1, fx - 1
        while sy <= (N - 1) and sx >= 1:
            second.append((sy, sx))
            sy += 1
            sx -= 1
        # 가능한 두번째 점 순회
        for sy, sx in second:
            ty, tx = sy - 1, sx - 1
            # 세번째 점 찾으면 (교차점)
            while True:
                # 범위 밖으로 벗어나면,
                if ty == y or tx < 0:
                    break

                # 교차점을 발견한다면,
                if (ty, tx) in last:
                    result.append((fy, fx))
                    result.append((sy, sx))
                    result.append((ty, tx))
                    max_v = max(max_v, dessert(result))
                    # 초기화
                    result = [(y, x)]

                ty -= 1
                tx -= 1

    return max_v


# 꼭짓점을 순회하며 디저트가게 목록 작성하는 함수
def dessert(lst):
    result = []
    y1, x1 = lst[0]
    y2, x2 = lst[1]
    y3, x3 = lst[2]
    y4, x4 = lst[3]

    ny, nx = y1, x1

    while ny != y2 and nx != x2:
        result.append(arr[ny][nx])
        ny += 1
        nx += 1

    while ny != y3 and nx != x3:
        result.append(arr[ny][nx])
        ny += 1
        nx -= 1

    while ny != y4 and nx != x4:
        result.append(arr[ny][nx])
        ny -= 1
        nx -= 1

    while ny != lst[0][0] and nx != lst[0][1]:
        result.append(arr[ny][nx])
        ny -= 1
        nx += 1

    # 겹치는 디저트 가게가 있는지 체크!
    length = len(result)
    length_set = len(set(result))

    if length == length_set:
        return length
    else:
        return -1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = -1
    # 시작점들을 순회하기
    for i in range(N-2):
        for j in range(1, N-1):
            ans = max(ans, square(i, j))
    print(f'#{tc} {ans}')