from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = 1 
    
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if visited[i] == 0:  
                visited[i] = -visited[node]  
                queue.append(i)
            elif visited[i] == visited[node]:  
                return False  
    return True

K = int(input())

for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)
    
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    is_bipartite = True
    for i in range(1, V + 1):
        if visited[i] == 0:
            if not bfs(graph, i, visited): 
                is_bipartite = False
                break

    print("YES" if is_bipartite else "NO")
