def BFS(start):
    global visited
    
    Q = []
    Q.append(start)
    visited[start] = 1

    while Q:
        now = Q.pop(0)

        for i in range(1, V + 1):
            if graph[now][i] == 1 and visited[i] == 0:
                Q.append(i)
                visited[i] = 1
                

# 테스트케이스 수
K = int(input())

# 각 테스트케이스에 대하여
for _ in range(K):
    
    # V = 정점, E = 간선
    V, E = map(int, input().split())

    # 인접행렬
    graph = [[0] * (V + 1) for _ in range(V + 1)]
    
    # 입력받은 간선들 인접행렬에 기록하기
    for _ in range(E):
        v1, v2 = map(int, input().split())
        graph[v1][v2] = 1
        graph[v2][v1] = 1
    
    # 방문정보
    visited = [0] * (V + 1)
    visited[0] = 1

    # 몇 개로 분할되는가?
    cnt = 0

    # 방문하지 않은 정점이라면 BFS 돌리기
    for v in range(V + 1):
        if v == 0:
            BFS(v)
            cnt += 1

    # 이분그래프 여부 확인
    if cnt == 2:
        print('YES')
    else:
        print('NO')