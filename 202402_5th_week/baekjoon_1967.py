# 트리의 지름
from collections import deque

# 거리를 파악하기 위한 BFS
def BFS(start):
    Q = deque()
    Q.append(start)
    visited = [-1] * (N + 1)
    visited[start] = 0

    # bfs 돌면서 시작 노드로부터의 거리를 visited 배열에 기록
    while Q:
        now = Q.popleft()
        for next in tree_dict[now]:
            next_node, distance = next
            if visited[next_node] == -1:
                Q.append(next_node)
                visited[next_node] = visited[now] + distance

    far_node = -1
    max_dist = -100
    
    for i in range(1, N + 1):
        if visited[i] >= max_dist:
            far_node = i
            max_dist = visited[i]
    
    # 시작 노드에서 가장 먼 노드와 그 거리를 리턴
    return (far_node, max_dist)


# 노드 갯수
N = int(input())

# 트리정보 입력할 dict 
tree_dict = {}
for i in range(1, N + 1):
    tree_dict[i] = []

# 입력받은 간선정보 입력
for _ in range(N - 1):
    parent, child, dist = map(int, input().split())
    tree_dict[parent].append((child, dist))
    tree_dict[child].append((parent, dist))

# 임의의 노드에서 BFS 돌리기
start_node, x = BFS(1)

# 트리 지름 구하기
end_node, result = BFS(start_node)

# 결과 출력
print(result)
