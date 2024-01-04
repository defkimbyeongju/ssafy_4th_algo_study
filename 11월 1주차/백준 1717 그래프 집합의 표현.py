import sys
input = sys.stdin.readline

# 루트 노드가 아니라면 루트 노드를 찾을 때까지 재귀적으로 호출
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union(x, y):
    x = find(x)
    y = find(y)
    
    if x != y:
        parent[y] = x

n, m = map(int, input().split())
parent = [i for i in range(n+1)]

for _ in range(m):
    op, a, b = map(int, input().split())
    
    if op == 0:
        union(a, b)
    elif op == 1:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
