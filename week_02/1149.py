# 집의 수 입력
N = int(input())
# 집별 빨강, 초록, 파랑으로 칠하는 비용
cost_list = [list(map(int, input().split())) for _ in range(N)]
# [이전 집이 빨강인 경우, 이전 집이 초록인 경우, 이전 집이 파랑인 경우]
former = list()

# 각 집의 비용에 대하여
for cost in cost_list:
    # 이전 집 정보가 존재할 경우
    if former:
        # 이번 집의 색깔과 다른 색깔 중 가장 작은 비용으로 선택
        former[0], former[1], former[2] = cost[0] + min(former[1], former[2]), cost[1] + min(former[0], former[2]), cost[2] + min(former[0], former[1])
    # 첫 번째 집인 경우
    else:
        former = [cost[0], cost[1], cost[2]]

# 색칠 비용 중 최솟값 출력
print(min(former))
