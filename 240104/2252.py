'''
# 실패한 코드
# 1번부터 N번까지 for문 순회하면서 맨 앞자리에 넣어보고 가능한지 체크하면서 안되면 다음 자리에 넣어보고 확인하면서 정렬하는 알고리즘
N,M = map(int,input().split())
height = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int, input().split())
    height[a].append(b) # a는 b보다 더 크다
result = []
def check(i): # i: 숫자
    for j in range(len(result)-1, -1, -1):
        if i in height[result[j]]:
            return j+1
    return 0
for i in range(1,N+1):
    result.insert(check(i), i)
print(*result)
'''

# 위상 정렬 알고리즘
# in, out 확인
# 인접 리스트 graph로 outdegree 노드 정보 담기
# indegree 리스트에 해당 노드보다 앞서 등장해야 하는 노드 개수 저장
from collections import deque

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)
for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b) # a는 b보다 더 크다
    indegree[b] += 1

def topology_sort():
    result = []
    q = deque()
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        result.append(now)
        for next in graph[now]:
            indegree[next] -= 1
            if indegree[next] == 0:
                q.append(next)
    return result
print(*topology_sort())
