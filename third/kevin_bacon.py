# 백준 1389 케빈-베이컨

def bfs(s,g): # bfs로 문제 해결
    queue = []
    visited = [0]*(N+1)
    queue.append(s)
    visited[s] = 1
    while queue:
        t = queue.pop(0)
        if t == g:
            return visited[t]-1
        for i in arr[t]:
            if visited[i] == 0:
                visited[i] = visited[t]+1
                queue.append(i)

N,M = map(int, input().split())
arr = [[] for _ in range(N+1)] # 인접 리스트 생성
for _ in range(M):
    a,b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
min_v = 21e8
for i in range(1,N+1):
    total = 0
    for j in range(1, N+1):
        total += bfs(i, j)
    if min_v > total: # 케빈 베이컨의 수가 가장 적을 때
        min_v = total # 값 최신화
        minimum = [i] # 최소값 인덱스를 리스트로 생성
    elif min_v == total:
        minimum.append(i) # 최소값이 같을 때, 리스트에 추가

print(minimum[0]) # 최소값이 같을 때는 번호가 가장 빠른 사람 출력