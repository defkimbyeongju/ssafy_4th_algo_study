T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    tunnel_list = []
    tunnel = dict()
    for _ in range(M):
        ay, ax, by, bx, C = map(int, input().split())
        tunnel.setdefault((ay, ax), [by, bx, C])
        tunnel_list.append((ay, ax))
    distance = [[9e9] * N for _ in range(N)]
    q = [(0, 0)]
    distance[0][0] = 0
    while q:
        y, x = q.pop(0)
