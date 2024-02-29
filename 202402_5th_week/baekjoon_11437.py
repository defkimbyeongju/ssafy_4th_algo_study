# LCA
import sys
from collections import deque
input = sys.stdin.readline

sys.setrecursionlimit(100000)

# 노드 갯수
N = int(input())

# 인접 dict
line_dict = {}
for i in range(1, N + 1):
    line_dict[i] = []

# 간선정보 입력받기
for _ in range(N - 1):
    v1, v2 = map(int, input().split())
    line_dict[v1].append(v2)
    line_dict[v2].append(v1)

# 부모자식 관계 너비우선 탐색을 통해 기록
def BFS(start):

    Q = deque()
    Q.append(start)
    visited = [0] * (N + 1)
    visited[start] = -1

    while Q:
        now = Q.popleft()
        for next in line_dict[now]:
            if not visited[next]:
                Q.append(next)
                visited[next] = now
    
    return visited

# # 부모정보 기록된 배열
parents = BFS(1)

# 1번 노드의 부모들 기록하기
def record1(node):
    global n1_parents
    n1_parents.append(node)

    # 만약 부모노드가 -1일 경우 루트노드인 1까지 온것이므로 stop
    if parents[node] == -1:
        return
    
    record1(parents[node])

# 2번 노드의 부모들 기록하기
def record2(node):
    global n2_parents
    n2_parents.append(node)

    # 만약 부모노드가 -1일 경우 루트노드인 1까지 온것이므로 stop
    if parents[node] == -1:
        return

    record2(parents[node])


# 공통조상 구하는 함수
def find_parent():
    for parent in n1_parents:
        if parent in n2_parents_set:
            print(parent)
            return


# 공통조상 문제 갯수
M = int(input())

# 문제 입력받기
for _ in range(M):
    a, b = map(int, input().split())

    # 조상 기록하기
    n1_parents = []
    n2_parents = []
    record1(a)
    record2(b)

    # 비교대상인 n2 의 부모는 검색 편의를 위해 set 으로 변경
    n2_parents_set = set(n2_parents)

    # 공통조상 출력!
    find_parent()
