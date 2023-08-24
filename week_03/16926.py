# 배열의 세로, 가로 길이 및 회전의 수 입력
N, M, R = map(int, input().split())
# 배열 입력
Aij = [list(map(int, input().split())) for _ in range(N)]
# 배열의 세로, 가로 중 더 작은 변 설정
short_side = min(N, M)

# 회전 부분 개수만큼 진행
for idx in range(short_side // 2):
    # 회전 부분을 담을 리스트 설정
    revolution = list()

    # 회전 부분 위쪽 - 위쪽 전부
    revolution.extend(Aij[idx][idx:M - idx])

    # 회전 부분 오른쪽 - 맨 위와 맨 아래는 제외한 오른쪽 부분
    for right_idx in range(idx + 1, N - 1 - idx):
        revolution.append(Aij[right_idx][M - 1 - idx])

    # 회전 부분 아래쪽 - 맨 오른쪽에서부터 맨 왼쪽 바로 전까지
    revolution.extend(Aij[N - 1 - idx][M - 1 - idx:idx:-1])

    # 회전 부분 왼쪽 - 맨 아래에서부터 맨 위 바로 전까지
    for left_idx in range(N - 1 - idx, idx, -1):
        revolution.append(Aij[left_idx][idx])

    # 회전 부분 돌리기
    for r in range(R % len(revolution)):
        first = revolution.pop(0)
        revolution.append(first)

    # 회전 부분 인덱스
    revolution_idx = 0

    # 회전 부분 위쪽 변경
    for top_idx in range(idx, M - idx):
        Aij[idx][top_idx] = revolution[revolution_idx]
        revolution_idx += 1

    # 회전 부분 오른쪽 변경
    for right_idx in range(idx + 1, N - 1 - idx):
        Aij[right_idx][M - 1 - idx] = revolution[revolution_idx]
        revolution_idx += 1

    # 회전 부분 아래쪽 변경
    for bottom_idx in range(M - 1 - idx, idx, -1):
        Aij[N - 1 - idx][bottom_idx] = revolution[revolution_idx]
        revolution_idx += 1

    # 회전 부분 왼쪽 변경
    for left_idx in range(N - 1 - idx, idx, -1):
        Aij[left_idx][idx] = revolution[revolution_idx]
        revolution_idx += 1

# 배열 출력
for row in range(N):
    print(*Aij[row])
