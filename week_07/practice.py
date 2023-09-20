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
def dfs(now):
    