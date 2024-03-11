V, E = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(E)]
edges.sort(key=lambda x: x[2])

parents = [i for i in range(V + 1)]

def find(n):
    if parents[n] == n:
        return n
    else:
        return find(parents[n])

def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

answer = 0

for edge in edges:
    a, b = parents[edge[0]], parents[edge[1]]
    if find(a) == find(b):
        continue
    else:
        union(a, b)
        answer += edge[2]

print(answer)