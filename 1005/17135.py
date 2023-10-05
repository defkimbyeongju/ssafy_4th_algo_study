N, M, D = map(int, input().split())
enemy = []
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(M):
        if row[M] == 1:
            enemy.append((i, j))
