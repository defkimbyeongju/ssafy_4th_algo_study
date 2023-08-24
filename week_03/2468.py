# copy 모듈 불러오기
import copy
# 배열의 행과 열의 개수 입력
N = int(input())
# 높이 리스트 설정
height_list = list()
# 최고 높이를 위한 변수 설정, 초기값 0
max_height = 0

# 높이 리스트 입력 및 최고 높이 확이
for n in range(N):
    raw = list(map(int, input().split()))
    height_list.append(raw)
    max_height = max(max(raw), max_height)

# 물에 잠기지 않는 안전한 영역의 최대 개수 변수 설정, 초기값 0
max_safety_area = 0

# 각각의 비의 양에 따라 진행
for height in range(0, max_height):
    # 안전한 영역의 개수 변수 설정
    safety_area = 0
    # 이번 높이에서의 물에 잠기지 않는 영역을 계산하기 위한 리스트 설정
    safety_area_list = copy.deepcopy(height_list)

    # 높이 리스트를 순회하며 BFS 진행
    for j in range(N):
        for i in range(N):
            if safety_area_list[j][i] > height:
                safety_area += 1
                queue = list()
                queue.append((j, i))
                safety_area_list[j][i] = -1

                while queue:
                    now_j, now_i = queue.pop(0)
                    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

                    for dj, di in directions:
                        if 0 <= now_j + dj < N and 0 <= now_i + di < N:
                            if safety_area_list[now_j + dj][now_i + di] > height:
                                # 이미 탐색한 영역의 경우 -1 값을 설정해 중복 탐색 예방
                                safety_area_list[now_j + dj][now_i + di] = -1
                                queue.append((now_j + dj, now_i + di))

    # 물에 잠기지 않는 안전한 영역의 최대 개수보다 많으면 최대 개수 최신화
    max_safety_area = max(max_safety_area, safety_area)

# 물에 잠기지 않는 안전한 영역의 최대 개수 출력
print(max_safety_area)
