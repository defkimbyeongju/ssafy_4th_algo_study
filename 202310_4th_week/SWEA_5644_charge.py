import pprint

def BFS(sy, sx, c, i):
    global MAP
    visited = [[0] * 11 for _ in range(11)]
    Q = [(sy, sx)]
    visited[sy][sx] = 1
    MAP[sy][sx].append(i)

    while Q:
        ny, nx = Q.pop(0)

        # 충전 범위 넘어가면 pass
        if visited[ny][nx] > c:
            continue


        for dy, dx in directions:
            new_y, new_x = ny + dy, nx + dx
            if 0 > new_y or 0 > new_x or new_y >= 11 or new_x >= 11:
                continue
            if visited[new_y][new_x]:
                continue

            Q.append((new_y, new_x))
            visited[new_y][new_x] = visited[ny][nx] + 1
            MAP[new_y][new_x].append(i)


def transfer(n):
    if n == 0:
        return (0, 0)
    elif n == 1:
        return (-1, 0)
    elif n == 2:
        return (0, 1)
    elif n == 3:
        return (1, 0)
    else:
        return (0, -1)


def charge(y1, x1, y2, x2):
    max_v = -1
    possible_bc_A = MAP[y1][x1]
    possible_bc_B = MAP[y2][x2]

    if possible_bc_A == [] and possible_bc_B == []:
        return 0

    elif possible_bc_A == [] and possible_bc_B:
        for bc in possible_bc_B:
            max_v = max(max_v, ap_power[bc])
        return max_v

    elif possible_bc_B == [] and possible_bc_A:
        for bc in possible_bc_A:
            max_v = max(max_v, ap_power[bc])
        return max_v

    else:
        for bc_a in possible_bc_A:
            for bc_b in possible_bc_B:
                if bc_a == bc_b:
                    max_v = max(max_v, (ap_power[bc_a] + ap_power[bc_b]) // 2)
                else:
                    max_v = max(max_v, ap_power[bc_a] + ap_power[bc_b])
        return max_v


T = int(input())
for tc in range(1, T+1):
    M, A = map(int, input().split())
    movement_A = list(map(int, input().split()))
    movement_B = list(map(int, input().split()))
    ap_power = [-1]
    MAP = [[[] for i in range(11)] for _ in range(11)]
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for i in range(1, A+1):
        X, Y, C, P = map(int, input().split())
        BFS(Y, X, C, i)
        ap_power.append(P)

    max_charge = 0
    ay, ax, by, bx = 1, 1, 10, 10
    max_charge += charge(ay, ax, by, bx)
    for j in range(M):
        dy1, dx1 = transfer(movement_A[j])
        dy2, dx2 = transfer(movement_B[j])
        ay += dy1
        ax += dx1
        by += dy2
        bx += dx2
        max_charge += charge(ay, ax, by, bx)

    print(f'#{tc} {max_charge}')