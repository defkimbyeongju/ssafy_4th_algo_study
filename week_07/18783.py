# 맵의 세로 크기, 가로 크기 입력
N, M = map(int, input().split())
# 맵 정보 리스트로 입력
map_info = [list(map(int, input().split())) for _ in range(N)]

# 땅 정보 리스트 설정
ground_info = list()
# 스노우맨 땅, 보석 땅 변수 설정
snowman, jewelry = 0, 0
# 맵을 순회하며
for y in range(N):
    # 새로운 세로 칸으로 이동
    start = False
    for x in range(M):
        # 땅이 있다면
        if map_info[y][x] != 0:
            # 스노우맨 땅 혹은 보석 땅일 경우
            if map_info[y][x] == 2:
                snowman = len(ground_info)
            if map_info[y][x] == 3:
                jewelry = len(ground_info)

            # 새로운 땅이 시작하지 않았다면
            if start is False:
                start = x

            # 이번 세로 칸의 마지막 칸일 경우
            if x == M - 1 and start is not False:
                ground_info.append((y, start, x))

        # 땅이 없다면
        else:
            # 새로운 땅이 시작했었다면
            if start is not False:
                # 땅 정보 리스트에 추가
                ground_info.append((y, start, x - 1))
                start = False

# 인접 딕셔너리 설정
adj_dict = dict()
# 땅 정보를 순회하며
for now_num, (now_y, now_start_x, now_end_x) in enumerate(ground_info):
    # 이번 땅과 인접 리스트 설정
    adj_list = list()
    # 그 땅과 인접한 땅 탐색
    for next_num, (next_y, next_start_x, next_end_x) in enumerate(ground_info):
        # 두 개의 땅이 서로 수직 이동 불가능하다면
        if next_end_x < now_start_x or next_start_x > now_end_x:
            continue

        # 인접 리스트에 추가
        adj_list.append(next_num)

    # 이번 땅 인접 정보 입력
    adj_dict[now_num] = adj_list


# 스노우맨 게임 진행
# 탐색 함수 설정
def vertical_movement(now):
    # 전역 변수 limit, snowman, is_arrived 설정
    global limit, snowman, is_arrived

    # 스노우맨에 도착 했을 때
    if now == snowman:
        is_arrived = True
        return
    
    # 스노우맨에 도착 하지 않았다면 다음 이동할 발판 탐색
    for next_ground in adj_dict[now]:
        # 다음 발판이 이미 이동 했던 발판일 경우 넘어가기
        if visited[next_ground]:
            continue

        # limit 보다 작아서 이동할 수 있는 발판에 대하여
        if abs(ground_info[next_ground][0] - ground_info[now][0]) <= limit:
            # 다음 발판으로 이동 했을 경우와 하지 않았을 경우에 대하여 진행
            visited[next_ground] = 1
            vertical_movement(next_ground)
            visited[next_ground] = 0


# 도착 여부 확인 변수 설정
is_arrived = False
# LIMIT 변수 설정
limit = 0
# 방문 여부 확인 변수 리스트로 설정
visited = [0] * len(ground_info)
# 시작점 방문 체크
visited[jewelry] = 1

# 스노우맨에 도착할 때까지 반복 진행
while not is_arrived:
    # LIMIT 값 늘리고 진행
    limit += 1
    vertical_movement(jewelry)

# 최소 LIMIT 값 출력
print(limit)
