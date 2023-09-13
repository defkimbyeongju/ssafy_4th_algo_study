# 테스트 케이스 개수 입력
T = int(input())
# 각각의 테스트 케이스에 대하여 진행
for tc in range(1, T + 1):
    # 지하철 역의 개수 입력
    N = int(input())
    # N개의 역의 이용자 수 리스트로 입력
    passenger_list = list(map(int, input().split()))
    # 최고의 타당도 변수 설정
    max_feasibility = 0

    # 첫 번째 역 선택
    for first in range(N):
        # 두 번째 역 선택
        for second in range(first + 2, N):
            # 세 번째 역 선택
            for third in range(second + 2, N):
                # 네 번째 역 선택
                for forth in range(third + 2, N):
                    # 만약 첫 번째 역과 네 번째 역이 인접하지 않았다면
                    if 2 <= (first + N - forth):
                        # 네 개의 역을 선택 했을 때 가능한 두 가지 경우에 대해 최고의 타탕도 확인
                        max_feasibility = max(max_feasibility, (passenger_list[first] + passenger_list[second]) ** 2 + (passenger_list[third] + passenger_list[forth]) ** 2)
                        max_feasibility = max(max_feasibility, (passenger_list[first] + passenger_list[forth]) ** 2 + (passenger_list[second] + passenger_list[third]) ** 2)

    # 최고의 타당도 출력
    print(f"#{tc} {max_feasibility}")
