def BFS(start):     # BFS 함수
    visited = [0] * (N + 1)     # visited 생성
    Q = []      # Q 생성
    Q.append(start)     # 인큐
    visited[start] = 1  # 시작점 방문 표시
    while Q:
        now = Q.pop(0)
        for i in range(1, N + 1):
            if arr[now][i] == 1 and not visited[i]:     # 아는 친구면
                Q.append(i)     # 인큐
                visited[i] = visited[now] + 1   # 몇다리 건너서 아는지 체크

    return sum(visited) - N     # 케빈 베이컨 수 리턴


N, M = map(int, input().split())    # 사람 수, 관계 수 입력
arr = [[0] * (N+1) for _ in range(N+1)]     # 관계 기록 배열
for _ in range(M):
    f1, f2 = map(int, input().split())      # 관계 입력 받기
    arr[f1][f2] = 1
    arr[f2][f1] = 1

bacon = [0] * (N+1)     # 각 사람의 케빈 베이컨 수 기록
for f in range(1, N+1): # 각 사람에 대하여
    bacon[f] = BFS(f)   # 케빈 베이컨 수 구하기

print(bacon.index(min(bacon[1:])))  # 케빈 베이컨 수가 가장 적은 사람 출력
