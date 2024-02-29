# 부모인 1번 노드에서 가장 멀리 떨어진 노드를 구하고, 해당 노드에서 가장 멀리 떨어진 노드를 구해서 둘 사이의 거리를 구하면 됨
# 거리 구하는 것은 bfs 방식으로 해결. 자료구조가 트리 형태이므로 한 노드에서 다른 노드까지 가는 방법이 1개임. 다익스트라는 활용할 필요 x
import sys
N = int(sys.stdin.readline())
tree = [[] for _ in range(N+1)] # 인접 리스트로 input 받기
for i in range(N-1):
    p1, p2, q = map(int, sys.stdin.readline().split())
    # 양방향 연결이기 때문에 양쪽에 다 추가해줌
    tree[p1].append([p2,q])
    tree[p2].append([p1,q])
def diameter(start):
    visited = [-1]*(N+1)
    max_distance = 0
    max_idx = start
    q = [[start, 0]]
    visited[start] = 0
    while q:
        node0, d0 = q.pop()
        for node1, d1 in tree[node0]:
            if visited[node1]==-1:
                visited[node1]=d0+d1
                if d0+d1>max_distance:
                    max_distance, max_idx = d0+d1, node1
                q.append([node1, d0+d1])
    return [max_idx, max_distance]
start = diameter(1)[0]
print(diameter(start)[1])