# copy 모듈 불러오기
import copy

# 테스트 케이스 입력
T = int(input())
# 각각의 테스트 케이스에 대해 진행
for tc in range(1, T + 1):
    # 지형의 한 변의 길이와 로봇이 동작 가능한 일 수 입력
    N, M = map(int, input().split())
    # 지형 정보 리스트 입력
    original = [list(map(int, input().split())) for _ in range(N)]
    # 네 방향 리스트 설정
    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    # 최대 수확 횟수 변수 설정
    max_harvest = 0

    # 회전 함수 설정
    def turn(n, pos_y, pos_x):  # n: 우선 순위에 해당 하는 작업 먼저 진행, pos_y ,pos_x: 현재 보는 방향
        # 오른쪽
        if n == 0:
            return pos_x, -pos_y
        # 앞쪽
        elif n == 1:
            return pos_y, pos_x
        # 왼쪽
        elif n == 2:
            return -pos_x, pos_y
        # 뒤쪽
        elif n == 3:
            return -pos_y, -pos_x

    # 지형 순회 하며 진행
    for y in range(N):
        for x in range(N):
            # 각각의 농지에 대하여 진행
            if original[y][x] == 0:
                # 각각의 방향에 대하여 진행
                for dir_y, dir_x in directions:
                    # 각각의 경우에 이용할 새로운 지형 정보 리스트 설정
                    topography = copy.deepcopy(original)
                    # 수확 횟수 변수 설정
                    harvest = 0
                    # 현재 위치 값 설정
                    now_y, now_x = y, x
                    # 매일 매일 진행
                    for day in range(1, M + 1):
                        # 오전
                        # 현재 농지가 빈 농지인 경우
                        if topography[now_y][now_x] % 100 == 0:
                            # 다음 농지가 빈 농지 혹은 곡식이 열린 농지일 경우
                            for d in range(4):
                                dy, dx = turn(d, dir_y, dir_x)
                                if topography[now_y + dy][now_x + dx] % 100 <= 1 and topography[now_y + dy][now_x + dx] != 1:
                                    # 씨 심기 수행
                                    topography[now_y][now_x] = 1 + topography[now_y][now_x] + (3 + topography[now_y][now_x] // 100 + 1) + 100 + 1
                                    break
                            # 다음 농지로 이동할 수 없는 경우
                        # 현재 농지에 곡식이 열린 경우
                        else:
                            # 수확 수행
                            topography[now_y][now_x] = topography[now_y][now_x] - 1
                            harvest += 1
                        # 오후
                        # 이동 가능한 곳이 있다면
                        for d in range(4):
                            dy, dx = turn(d, dir_y, dir_x)
                            if topography[now_y + dy][now_x + dx] % 100 <= 1 and topography[now_y + dy][now_x + dx] != 1:
                                # 이동 수행
                                now_y, now_x = now_y + dy, now_x + dx
                                dir_y, dir_x = dy, dx
                                break
                        # 이동 가능한 곳이 없다면

                        # 하루가 지날 경우
                        # 새로운 지형 정보 리스트에서
                        for end_y in range(N):
                            for end_x in range(N):
                                # 싹이 났다면
                                if topography[end_y][end_x] % 100 > 1:
                                    # 일수 차감 수행
                                    topography[end_y][end_x] = topography[end_y][end_x] - 1

                    # 최대 수확 횟수 확인
                    max_harvest = max(max_harvest, harvest)\

    # 정답 출력
    print(f"#{tc} {max_harvest}")
