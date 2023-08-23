n = int(input())
a, b = map(int, input().split())
m = int(input())
arr = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    p, c = map(int, input().split())
    arr[p][c] = arr[c][p] = 1
visited = [0] * (n+1)
q = [a]
visited[a] = 1
while q:
    t = q.pop(0)
    for i in range(n+1):
        if arr[t][i] and not visited[i]:
            q.append(i)
            visited[i] = visited[t] + 1
if visited[b]:
    print(visited[b] - 1)
else:
    print(-1)
