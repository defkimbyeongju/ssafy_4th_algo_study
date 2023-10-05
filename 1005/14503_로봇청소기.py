def clean_room(r, c, d, room):
    # 방향 전환 (북, 동, 남, 서)
    dx = [0,1,0,-1]
    dy = [-1,0,1,0]

    def turn_left(direction):
        direction = (direction - 1) % 4
        return direction
    
    # 초기값
    room[r][c] = 2
    cnt = 1
    
    # 현재 칸의 주변 4칸 탐색
    while True:
        # 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
        if room[r-1][c]!=0 and room[r][c+1]!=0 and room[r+1][c]!=0 and room[r][c-1]!=0:
            # 2-1. 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면
            if room[r - dy[d]][c - dx[d]] !=1:
                r -= dy[d]
                c -= dx[d]
            # 한 칸 후진
            # 2-2. 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면
            else:
                break
            # 작동을 멈춘다.
        else:
            # 3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
            # 3-1. 반시계 방향으로 90도 회전
            d = turn_left(d)
            # 3-2. 빈칸일 경우 그 방향으로 한 칸 전진
            if room[r + dy[d]][c + dx[d]] == 0:
                r += dy[d]
                c += dx[d]
                # 1. 현재칸이 청소되지 않은 경우 청소
                room[r][c] = 2
                cnt += 1
            # 빈칸이 아닌 경우 청소되지 않은 빈 칸을 찾을 때까지 반시계방향 회전
            else:
                continue
    return cnt
    

N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
ans = clean_room(r, c, d, room)
print(ans)

