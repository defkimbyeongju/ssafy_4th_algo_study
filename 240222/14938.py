from collections import deque

n, m, r = map(int, input().split())
items = [0] * (n + 1)
for i, t in enumerate(list(map(int, input().split())), 1):
    items[i] = t
# areas = [0, 5, 7, 8, 2, 3]
    
connected = [[] for _ in range(n + 1)]
for _ in range(r):
    a, b, l = map(int, input().split())
    connected[a].append((b, l))
    connected[b].append((a, l))
# connected = [[], [(4, 5), (2, 3)], [(5, 4), (3, 3), (1, 3)], [(2, 3)], [(1, 5)], [(2, 4)]]
    
answer = 0
for area in range(1, n + 1):
    dijk = [9e9] * (n + 1)
    q = deque()
    q.append([area, 0])
    dijk[area] = 0
    while q:
        now, moved = q.popleft()
        for next, distance in connected[now]:
            if dijk[next] >= moved + distance:
                q.append([next, moved + distance])
                dijk[next] = moved + distance
    answer = max(answer, sum([items[i] for i, t in enumerate(dijk) if t <= m]))

print(answer)