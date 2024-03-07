from collections import deque
N = int(input())
M = int(input())
linked = [list(map(int, input().split())) for _ in range(N)]
adj_arr = [[] for _ in range(N+1)]
cities = list(map(int, input().split()))
for i in range(N):
    for j in range(N):
        if linked[i][j]:
            if j+1 not in adj_arr[i+1]:
                adj_arr[i+1].append(j+1)
            if i+1 not in adj_arr[j+1]:
                adj_arr[j+1].append(i+1)

def go(node1, node2):
    used = [0] * (N+1)
    used[node1] = 1
    q = deque()
    q.append(node1)
    while q:
        now = q.popleft()
        for i in adj_arr[now]:
            if not used[i]:
                q.append(i)
                used[i] = 1
    if used[node2]:
        return True
    return False
for i in range(M-1):
    temp = go(cities[i], cities[i+1])
    if not temp:
        print('NO')
        break
else:
    print('YES')