import sys
sys.setrecursionlimit(10**7)  # 백준에서 문제 풀다가 런타임 에러(recurssion error)뜨면 사용해보길!

def dfs(y, x):
    dir = [(0,1), (0,-1), (-1,0), (1,0)]
    for k,p in dir:
        dy, dx = y+k, x+p
        if 0<=dy<N and 0<=dx<M:
            if arr[dy][dx] == 1 and visited[dy][dx] == 0:
                visited[dy][dx] = 1
                dfs(dy, dx)

T = int(input())

for _ in range(T):  # test 반복
    result = 0  # 결과 변수
    M,N,K = map(int, input().split())  # M은 가로길이(열의 개수), N은 세로길이(행의 개수), K는 배추 개수
    arr = [[0]*M for _ in range(N)]  # 배추 위치를 표시할 빈 배열
    visited = [[0] * M for _ in range(N)] # 방문 여부 확인할 배열
    for _ in range(K):
        a, b = map(int, input().split()) # 배추 위치 좌표 입력받고 표시
        arr[b][a] = 1
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1 and visited[i][j] == 0:
                visited[i][j] = 1
                dfs(i, j) # dfs 통해 인접 부분 탐색하고 체크해주기
                result += 1
    print(result)
