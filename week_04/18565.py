# 테스트 케이스 개수 입력
T = int(input())
# 각각의 테스트 케이스에 대하여 진행
for tc in range(1, T + 1):
    # 풍선의 개수 입력
    N = int(input())
    # 풍선의 점수에 대한 정보 리스트로 입력
    balloons_list = list(map(int, input().split()))
    # 최대 점수 변수 설정
    max_score = 0

    # 사격 진행 함수 설정
    def shoot(i, k, score):
        global max_score
        # 모든 풍선을 사격 했을 때
        if i == k:
            # 최대 점수 확인
            max_score = max(max_score, score)
        # 사격할 풍선이 남아 있다면
        else:
            # 사격 되지 않은 풍선에 대하여
            for j in range(N):
                if balloons_list[j]:
                    # 사격한 풍선에 적힌 점수 변수 설정
                    j_balloon = balloons_list[j]
                    # 좌우로 이웃하는 풍선에 적힌 숫자 확인 및 점수 계산
                    j_left, j_right = j - 1, j + 1
                    while j_left > -1:
                        if balloons_list[j_left] != 0:
                            break
                        else:
                            j_left -= 1
                    while j_right < N:
                        if balloons_list[j_right] != 0:
                            break
                        else:
                            j_right += 1
                    if j_left == -1 and j_right == N:
                        j_score = balloons_list[j]
                    elif j_left == -1:
                        j_score = balloons_list[j_right]
                    elif j_right == N:
                        j_score = balloons_list[j_left]
                    else:
                        j_score = balloons_list[j_left] * balloons_list[j_right]
                    # 이미 사격한 풍선 점수 초기화
                    balloons_list[j] = 0
                    # 다음 사격 진행
                    shoot(i + 1, k, score + j_score)
                    # 이전 사격 현황 초기화
                    balloons_list[j] = j_balloon

    # 사격 진행
    shoot(0, N, 0)
    # 최대 점수 출력
    print(f"#{tc} {max_score}")
