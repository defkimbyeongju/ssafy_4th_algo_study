def find_apple():   # 지도에서 사과의 좌표 찾는 함수
    apple = {}  # 찾은 사과의 좌표를 저장할 dict
    for i in range(N):
        for j in range(N):      # 지도를 순회하면서
            if arr[i][j] != 0:  # 사과 발견하면
                apple[arr[i][j]] = (i, j)   # 해당 사과 넘버링과 좌표 dict에 저장
    return apple    # 만들어진 사과 dict 리턴


def route():    # 사과 루트를 순회하며 회전횟수 정답도출할 함수
    quantity = len(find_apple())    # 사과 개수
    apple_loc = find_apple()        # 찾을 사과 좌표
    rotate = 0                      # 총 회전 횟수 저장
    direction_Q = ['Down', 'Left', 'Up', 'Right']   # 우회전 할때마다 Q로 돌릴 방향
    now_y, now_x = 0, 0             # 0,0 부터 시작
    route_Q = ['Right']             # 현재 진행 방향 저장
    for i in range(1, quantity + 1):    # 총 사과 개수만큼
        ay, ax = apple_loc[i]           
        if now_y < ay and now_x < ax:   # 만약 사과 좌표가 현재 좌표 기준 (+, +) 이면
            # 오른쪽으로 진행, 아래로 진행 과정이 필요
            while 'Right' not in route_Q or 'Down' not in route_Q:  # 방향 맞을때 까지
                d = direction_Q.pop(0)  # Q에서 방향 꺼내기
                direction_Q.append(d)   # Q에 넣어주고
                route_Q.append(d)       # 현재 진행방향에 추가
                rotate += 1             # 회전횟수 1 추가
            # 끝나면, 현재진행방향 초기화
            route_Q = route_Q[-1:-2:-1]
            now_y, now_x = ay, ax   # 현재 좌표를 수정
        elif now_y < ay and now_x > ax:
            while 'Left' not in route_Q or 'Down' not in route_Q:
                d = direction_Q.pop(0)
                direction_Q.append(d)
                route_Q.append(d)
                rotate += 1
            route_Q = route_Q[-1:-2:-1]
            now_y, now_x = ay, ax
        elif now_y > ay and now_x < ax:
            while 'Right' not in route_Q or 'Up' not in route_Q:
                d = direction_Q.pop(0)
                direction_Q.append(d)
                route_Q.append(d)
                rotate += 1
            route_Q = route_Q[-1:-2:-1]
            now_y, now_x = ay, ax
        elif now_y > ay and now_x > ax:
            while 'Left' not in route_Q or 'Up' not in route_Q:
                d = direction_Q.pop(0)
                direction_Q.append(d)
                route_Q.append(d)
                rotate += 1
            route_Q = route_Q[-1:-2:-1]
            now_y, now_x = ay, ax

    return rotate


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc} {route()}')
