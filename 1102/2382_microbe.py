T = int(input())
for tc in range(1,T+1):
    N,M,K = map(int,input().split())
    microbes = [list(map(int, input().split())) for _ in range(K)]
    directions = [(-1,0),(1,0),(0,-1),(0,1)] # 1,2,3,4 상하좌우
    while M > 0:
        for i in range(len(microbes)): # 각자의 방향으로 1칸씩 이동
            y,x,power,dir = microbes[i]
            dy, dx = directions[dir-1]
            ny, nx = y+dy, x+dx
            if ny == 0 or ny == N-1 or nx == 0 or nx == N-1: # 테두리에 닿으면
                power//=2 # 파워 절반으로 감소
                # 방향 바꿔주기
                if dir%2 == 0: # 짝수면 반대 방향은 -1
                    dir -= 1
                else:
                    dir += 1
            microbes[i] = ny,nx,power,dir
        microbes.sort(key=lambda x:(x[0],x[1],x[2]))
        prev_y, prev_x = -1, -1
        for k in range(len(microbes)):
            y,x,p,d = microbes[k][0], microbes[k][1], microbes[k][2], microbes[k][3]
            if y == prev_y and x == prev_x: # 이전과 좌표가 겹치면
                p += microbes[k-1][2]
                microbes[k-1] = [prev_y, prev_x, 0, d]
                microbes[k] = [y,x,p,d]
            prev_y, prev_x = y, x
        M -= 1

    res = 0
    for i in range(len(microbes)):
        res += microbes[i][2]
    print(f'#{tc} {res}')
