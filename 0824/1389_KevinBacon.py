N, M = map(int, input().split())
arr = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    m1, m2 = map(int, input().split())
    arr[m1][m2] = arr[m2][m1] = 1
min_kb = N * N
for i in range(1, N+1):
    visited = [0] * (N+1)
    q = [i]
    visited[i] = 1
    while q:
        t = q.pop(0)
        for j in range(1, N+1):
            if arr[t][j] and not visited[j]:
                q.append(j)
                visited[j] = visited[t] + 1
    if min_kb > sum(visited):
        min_kb = sum(visited)
        ans = i
print(ans)
