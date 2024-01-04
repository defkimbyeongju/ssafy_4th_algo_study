from collections import deque

N, M = map(int, input().split())
A = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1) # 진입 차수 리스트

for i in range(M):
    S, E = map(int, input().split()) # 인접 리스트 데이터 저장
    A[S].append(E)
    indegree[E] += 1

queue = deque()

for i in range(1, N + 1):
    if indegree[i] == 0: # 진입 차수 리스트의 값이 0인 학생을 큐에 삽입
        queue.append(i)

while queue:
    now = queue.popleft()
    print(now, end=' ') # 현재 노드값 출력
    for next in A[now]:
        indegree[next] -= 1 # 타깃 노드 진입 차수 리스트 값 1 감소
        if indegree[next] == 0: # 진입 차수가 0이면
            queue.append(next) # 큐에 타깃 노드 추가