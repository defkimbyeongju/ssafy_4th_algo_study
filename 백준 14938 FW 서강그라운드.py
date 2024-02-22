import sys

input = sys.stdin.readline


def floydWarshall(n, dist):
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))

INF = float("inf")
dist = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dist[i][i] = 0

for _ in range(r):
    a, b, l = map(int, input().split())
    dist[a][b] = l
    dist[b][a] = l

floydWarshall(n, dist)

max_items = 0
for i in range(1, n + 1):
    total = 0
    for j in range(1, n + 1):
        if dist[i][j] <= m:
            total += items[j]
    max_items = max(max_items, total)

print(max_items)
