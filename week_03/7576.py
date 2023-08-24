# copy 모듈 불러오기
import copy
# 상자의 가로 칸의 수와 세로 칸의 수 입력
M, N = map(int, input().split())
# 토마토 상자 리스트 설정
tomato_box = list()
# 토마토가 담겨 있는 상자 좌표 리스트 설정
tomato_list = list()
# 익지 않은 토마토의 수
unripe_tomato = 0

# 토마토 상자 리스트 입력
for n in range(N):
    row = list(map(int, input().split()))
    for m in range(M):
        # 토마토 상자에 토마토가 들어 있는 경우
        if row[m] == 1:
            # 토마토가 담겨 있는 상자 좌표 리스트 추가
            tomato_list.append((n, m))
        # 익지 않은 토마토가 들어 있는 경우
        elif row[m] == 0:
            # 익지 않은 토마토의 수 증가
            unripe_tomato += 1
    # 토마토 상자 리스트에 입력 추가
    tomato_box.append(row)

# 토마토가 익는데 영향을 주는 방향 리스트
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# 토마토가 익을 때까지의 날짜 변수 설정
day = 0

# 익지 않은 토마토가 있다면 반복
while unripe_tomato:
    # 하루 경과
    day += 1
    # 새롭게 익은 토마토의 좌표 리스트 설정
    new_tomato = list()
    # 토마토 리스트에 대하여 진행
    for tomato_y, tomato_x in tomato_list:
        # 영향을 주는 영역에 익지 않은 토마토가 있는 경우
        for dy, dx in directions:
            if 0 <= tomato_y + dy < N and 0 <= tomato_x + dx < M and tomato_box[tomato_y + dy][tomato_x + dx] == 0:
                # 토마토 익히기
                tomato_box[tomato_y + dy][tomato_x + dx] = 1
                # 익지 않은 토마토 수 감소
                unripe_tomato -= 1
                # 새롭게 익은 토마토의 좌표 리스트에 좌표 추가
                new_tomato.append((tomato_y + dy, tomato_x + dx))

    # 새롭게 익은 토마토가 존재하는 경우
    if new_tomato:
        # 새롭게 익은 토마토에 대하여 하루 경과 후 다시 진행
        tomato_list = copy.deepcopy(new_tomato)
    # 새롭게 익은 토마토가 존재하지 않은 경우
    else:
        # 종료
        break

# 익지 않은 토마토가 존재하는 경우
if unripe_tomato:
    # 토마토가 모두 익지는 못하는 상황 출력
    print(-1)
# 모든 토마토가 익은 경우
else:
    # 토마토가 모두 익을 때까지의 최소 날짜 출력
    print(day)
