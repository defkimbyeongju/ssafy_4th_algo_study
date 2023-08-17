# 테스트 케이스 개수 입력
T = int(input())
# 각각의 테스트 케이스에 대하여 진행
for tc in range(T):
    # 배추밭의 가로, 세로, 배추가 심어져 있는 위치의 개수 입력
    M, N, K = map(int, input().split())
    # 배추가 심어져 있는 좌표
    cabbage_field = [list(map(int, input().split())) for _ in range(K)]
    # 배추흰지렁이 영향 좌표 리스트 설정
    worm_field = list()
    # 배추흰지렁이 마리수 설정
    worm = 0
    # 방향 설정
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    # 이전의 좌표 리스트 설정
    formal = list()

    # 배추가 심어져 있는 좌표에 대하여 진행
    for cabbage_y, cabbage_x in cabbage_field:
        # 배추가 심어져 있는데 배추흰지렁이 투입이 되지 않았을 경우
        if [cabbage_y, cabbage_x] not in worm_field:
            # 배추흰지렁이 투입
            worm += 1
            # 배추흰지렁이 투입 좌표의 영향 영역 확인
            while True:
                # 네 방향에 대하여 진행
                for i in range(4):
                    nearby_cabbage = [cabbage_y + dy[i], cabbage_x + dx[i]]

                    # 인접 영역에 배추가 심어져 있고 배추흰지렁이 영향 좌표에 포함되지 않는 경우
                    if nearby_cabbage in cabbage_field and nearby_cabbage not in worm_field:
                        worm_field.append(nearby_cabbage)
                        formal.append(nearby_cabbage)
                        cabbage_y, cabbage_x = nearby_cabbage[0], nearby_cabbage[1]
                        break
                else:
                    # 인접 영역에 배추흰지렁이가 영향을 끼칠 좌표가 없는데 이전의 좌표가 존재할 경우
                    if formal:
                        # 이전의 좌표 탐색 중지
                        formal.pop()
                        # 한 단계 윗 단계로 돌아가 탐색 재시도
                        if formal:
                            cabbage_y, cabbage_x = formal[-1][0], formal[-1][1]
                        # 윗 단계가 존재하지 않을 경우 탐색 종료
                        else:
                            break
                    # 이전의 좌표가 없는 경우 탐색 종료
                    else:
                        break

    # 배추흰지렁이 마리수 출력
    print(worm)
