# 트리의 부모 찾기
from collections import deque

# BFS
def BFS(start):
    
    global parents

    Q = deque()
    Q.append(start)
    visited = [0] * (N + 1)
    visited[1] = 1
    
    # BFS 돌리기
    while Q:
        now = Q.popleft()
        for next in line_list[now]:     # 인접한 노드를 루트부터 순서대로 내려가며
            if not visited[next]:           
                Q.append(next)
                visited[next] = 1       
                parents[next] = now     # 부모노드 저장하기
    

# 노드 갯수
N = int(input())

# 인접리스트
line_list = [[] for i in range(N + 1)]

# 인접리스트 정보 입력
for i in range(N - 1):
    a, b = map(int, input().split())
    line_list[a].append(b)
    line_list[b].append(a)

# 부모노드
parents = [0] * (N + 1)

# 너비우선탐색 돌리기
BFS(1)

# 저장된 부모노드 값 순서대로 출력
for j in range(2, N + 1):
    print(parents[j])