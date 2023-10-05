# baekjoon 14891번 톱니바퀴

# 시작되는 톱니바퀴와 회전방향을 입력받아 톱니바퀴들을 회전여부를 체크하는 함수
def rotation_check(n, d):
    gear_status = [0, 0, 0, 0, 0]   # 기어 회전방향 기록
    gear_status[n] = d              # 출발하는 기어 회전방향 기록하기

    # 각 기어 별 좌,우 측 톱니체크
    connection = [[0, 0]]
    for gear in gears:
        connection.append([gear[6], gear[2]])

    tmp_n = n
    tmp_d = d
    # 해당 기어 위로 가면서 동력전달 체크
    while tmp_n < 4:
        # 만일, 동일한 극이라면 회전전달이 되지 않으므로 종료
        if connection[tmp_n][1] == connection[tmp_n+1][0]:
            break
        # 동력전달은 기어 반대방향으로!
        gear_status[tmp_n+1] = -tmp_d
        tmp_n += 1
        tmp_d = -tmp_d

    tmp_n = n
    tmp_d = d
    # 해당 기어 아래로 가면서 동력전달 체크
    while tmp_n > 1:
        # 만일, 동일한 극이라면 회전전달 x
        if connection[tmp_n][0] == connection[tmp_n-1][1]:
            break
        gear_status[tmp_n-1] = -tmp_d
        tmp_n -= 1
        tmp_d = -tmp_d

    return gear_status


# 톱니바퀴 번호와 회전방향 입력받아 톱니바퀴 회전시키는 함수
def rotate(n, d):
    global gears

    # 방향 별로 회전시키기
    if d == 1:
        tmp = gears[n-1].pop()
        gears[n-1].insert(0, tmp)

    elif d == -1:
        tmp = gears[n-1].pop(0)
        gears[n-1].append(tmp)


gears = [list(map(int, input())) for _ in range(4)]
K = int(input())
for _ in range(K):
    N, D = map(int, input().split())
    result = rotation_check(N, D)
    for i in range(1, 5):
        rotate(i, result[i])
# 점수 계산
score = 0
for j in range(4):
    if gears[j][0] == 1:
        score += 2 ** j
print(score)
