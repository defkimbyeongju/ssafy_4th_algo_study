from collections import deque
N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def bfs(y, x):
    movelist = [(y, x)]
    sum = arr[y][x]
    cnt = 1
    queue = deque()
    queue.append((y, x))

    while queue:
        p, q = queue.popleft()
        now = arr[p][q]

        for dp, dq in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            np, nq = p + dp, q + dq
            if 0 <= np < N and 0 <= nq < N and (np, nq) not in movelist:
                next = arr[np][nq]

                if L <= abs(next - now) <= R:
                    queue.append((np, nq))
                    movelist.append((np, nq))
                    sum += next
                    cnt += 1

    return movelist, sum, cnt

answer = 0

while True:
    moves = []
    visited = [[False] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                mlist, msum, mcnt = bfs(i, j)
                mavg = msum // mcnt

                if mcnt > 1:
                    moves.append(mlist)
                    moves.append(mavg)

                for mi, mj in mlist:
                    visited[mi][mj] = True

    if moves:
        answer += 1
        for k in range(0, len(moves), 2):
            p = moves[k + 1]
            for pi, pj in moves[k]:
                arr[pi][pj] = p

    else:
        break
    
print(answer)