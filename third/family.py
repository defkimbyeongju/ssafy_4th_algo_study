# 백준 2644번 촌수계산

# 전형적인 bfs 문제

def bfs(a,b):
    queue = []
    queue.append(a)
    visited = [0]*(n+1)
    visited[a] = 1
    while queue:
        t = queue.pop(0)
        if t == b:
            return visited[t]-1 # 타겟을 만나면 visited 값 반환
        for i in arr[t]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[t] + 1 # 가족에 해당하면 거리를 증가시키며 탐색하기
    return -1 # 가족이 아니면 -1 출력



n = int(input())
a, b = map(int, input().split())
m = int(input())
arr = [[] for _ in range(n+1)] # 인접 리스트 만들어주기
for _ in range(m):
    x, y = map(int,input().split())
    arr[x].append(y)
    arr[y].append(x)

print(bfs(a,b))
