def BFS(start, end):    # BFS 탐색 함수
    visited = [0] * (N + 1)     # visited 생성
    Q = []                      # Q 생성
    Q.append(start)             # 인큐
    visited[start] = 1          # visited 에 추가
    while Q:
        now = Q.pop(0)  # 디큐
        if now == end:  # 목적지면
            return visited[now] - 1     # 거리 측정
        # bfs 탐색
        for i in range(1, N + 1):
            if arr[now][i] == 1 and not visited[i]:
                Q.append(i)
                visited[i] = visited[now] + 1

    return -1   # 연결되지 않으면 -1 리턴


N = int(input())    # 사람 수
p1, p2 = map(int, input().split())  # 촌수 계산 할 두 명
M = int(input())    # 부자 관계(간선)
arr = [[0] * (N+1) for _ in range(N+1)]     # 간선 정보 arr
for _ in range(M):  # 간선 입력받기
    n1, n2 = map(int, input().split())
    arr[n1][n2] = 1
    arr[n2][n1] = 1
print(BFS(p1, p2))  # 함수 호출
