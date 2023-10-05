# deque 모듈 불러오기
from collections import deque

# 지도의 세로 크기 N, 가로 크기 M 변수 입력
N, M = map(int, input().split())
# 연구소 지도 lab 변수 리스트로 설정 및 입력
lab = list()
for _ in range(N):
    lab.extend(list(map(int, input().split())))
# 안전 영역 크기의 최대값 변수 설정
max_safe = 0


# 새로운 벽을 세운 후에 안전 영역의 크기 구하는 함수 설정
def safe(i, wall):
    # 전역 변수 설정
    global N, M, max_safe
    
    # 벽을 3개 다 세웠을 경우
    if wall == 3:
        # 바이러스 확산 여부 확인 리스트 설정
        virus = [0] * (N * M)
        # 바이러스 리스트에 대하여
        for index in range(N * M):
            # 만약 현재 인덱스 공간이 바이러스가 있는데 확산이 되지 않았다면
            if lab[index] == 2 and virus[index] == 0:
                # 현재 바이러스부터 확산된 바이러스 bfs로 확인
                virus[index] = 1
                queue = deque()
                queue.append(index)
                directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

                while queue:
                    n, m = divmod(queue.popleft(), M)
                    for dn, dm in directions:
                        next_n = n + dn
                        next_m = m + dm

                        if 0 <= next_n < N and 0 <= next_m < M:
                            if lab[next_n * M + next_m] == 1 or virus[next_n * M + next_m] == 1:
                                continue

                            virus[next_n * M + next_m] = 1

                            queue.append(next_n * M + next_m)
        
        # 안전 영역 확인 후 최대 값이라면 최신화
        max_safe = max(max_safe, virus.count(0) - lab.count(1))

        return
    
    # 이전에 선택된 벽 이후의 공간에 대하여
    for index in range(i, N * M):
        # 현재 인덱스 공간의 상태 변수 설정
        space = lab[index]

        # 현재 인덱스 공간이 비어있다면
        if space == 0:
            # 현재 인덱스 공간에 벽을 세우고 다음 벽 세울 공간 탐색
            lab[index] = 1
            safe(index + 1, wall + 1)
            lab[index] = space


# 함수 실행
safe(0, 0)
# 안전 영역 크기의 최댓값 출력
print(max_safe)
