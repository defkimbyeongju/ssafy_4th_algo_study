import sys  # 빠른 입력을 위한 모듈
from collections import deque   # deque 사용하기 위해 모듈 import

N, M, R = map(int, sys.stdin.readline().split())     # 배열 크기와 회전횟수 입력받기
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]   # 초기 배열 설정
result = [[0] * M for _ in range(N)]    # 회전한 배열 기록할 빈 배열


# 각 테두리 별로 회전시키는 함수
def rotate(y1, x1, y2, x2):     # (y1, x1) 과 (y2, x2) 사각형의 테두리를 회전
    global result               # 회전 결과를 빈 배열 result 에 기록
    Q = deque()                 # 각 테두리를 회전시키기 위해 Q 를 생성
    if y1 <= y2 and x1 <= x2:   # 사각형이 반전되지 않도록
        # Q에 테두리를 시계방향 순서대로 집어넣기
        for i in range(x1, x2):
            Q.append(arr[y1][i])
        for j in range(y1, y2):
            Q.append(arr[j][x2])
        for k in range(x2, x1-1, -1):
            Q.append(arr[y2][k])
        for l in range(y2-1, y1, -1):
            Q.append(arr[l][x1])
        # 회전 횟수만큼 pop(0) 와 push 를 Q에 실행하여 시계반대방향으로 돌리는 효과
        r = R % len(Q)      # 의미없는 회전을 막기 위해 Q로 나눈 나머지 만큼만 회전
        for _ in range(r):
            tmp = Q.popleft()
            Q.append(tmp)
        # 회전완료된 Q를 result에 기록
        for i in range(x1, x2):
            result[y1][i] = Q.popleft()
        for j in range(y1, y2):
            result[j][x2] = Q.popleft()
        for k in range(x2, x1 - 1, -1):
            result[y2][k] = Q.popleft()
        for l in range(y2 - 1, y1, -1):
            result[l][x1] = Q.popleft()

        # 제일 안쪽 사각형이 아니라면 안쪽 사각형으로 이동하여 동일과정 반복
        if y1 != y2 and x1 != x2:
            rotate(y1+1, x1+1, y2-1, x2-1)


rotate(0, 0, N-1, M-1)      # 함수 호출

for lst in result:      # 결과 출력
    print(*lst)
