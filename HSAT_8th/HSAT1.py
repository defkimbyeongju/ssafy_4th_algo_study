import sys
from collections import deque

sys.stdin = open('HSAT1.txt')
input = sys.stdin.readline

# 점개수 10만
# 선개수 10만
# 시작 사람 2 ~ 10까지

# 점개수, 선개수, 시작사람
n, m, k = map(int, input().split())

result = float('inf')

graph = [[] for _ in range(n+1)]

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)

방문객 = set(map(int, input().split()))

모든사람 = set([i for i in range(1, n+1)])
전시관 = 모든사람 - 방문객

def bfs(전시관, 시작):
    q = deque([(시작, 0)])

    while q:
        now, dist = q.popleft()
        visited[now] = True
        if now == 전시관:
            return dist
        for next in graph[now]:
            if not visited[next]:
                q.append((next, dist + 1))
    
    return -1


for j in 전시관:
    temp = 0
    cnt = 0
    for p in 방문객:
        visited = [False] * (n+1)
        dist = bfs(j, p)
        if dist != -1: # 만약 갈 수 있다면 
            temp = max(temp, dist) # 갱신하고
            cnt += 1 #
    if cnt == len(방문객): # cnt가 len(방문객)이랑 똑같다 ==> 방문객들이 모두 그 전시관을 방문할 수 있다.   
        result = min(result, temp)
    

if result == float('inf'):
    print(-1)
else:
    print(result)


