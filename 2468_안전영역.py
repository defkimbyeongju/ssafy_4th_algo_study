import sys      # 빠른 입력을 위한 모듈
import copy     # 깊은 복사를 위한 모듈


def max_height(arr):    # 지도에서 가장 높은 땅의 높이 찾는 함수
    height = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > height:
                height = arr[i][j]
    return height


def safe_place(rain):   # 비 내리는 양을 받아서 그만큼 내렸을 때 안전지역 개수 체크하는 함수
    rain_map = copy.deepcopy(arr)   # visited 정보 체크할 배열 초기화
    cnt = 0     # 안전지역 수
    for i in range(N):
        for j in range(N):              # 지도를 순회하면서,
            if rain_map[i][j] > rain:   # 잠기지 않는 지역 발견하면
                cnt += 1                # 안전지역 +1
                Q = []                  # 아래 부터는 해당 지역에 연결된 지역을 방향배열로
                Q.append((i, j))        # 순회하면서 체크하고
                rain_map[i][j] = rain   # 해당 지역 수치를 rain 으로 낮춰 다시 순회 시 걸리지 않게 (visited 대용)
                while Q:
                    y, x = Q.pop(0)
                    for dy, dx in direction:
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < N and 0 <= nx < N and rain_map[ny][nx] > rain:
                            Q.append((ny, nx))
                            rain_map[ny][nx] = rain
    return cnt      # 안전지역 수 리턴


N = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
H = max_height(arr)
ans = 0
for i in range(H+1):    # 비가 오지 않을때 부터 모두 잠기는 때까지 각 비내리는 양에 대하여
    if safe_place(i) > ans:     # 최대 안전지역 수 저장
        ans = safe_place(i)

print(ans)  # 결과 출력
