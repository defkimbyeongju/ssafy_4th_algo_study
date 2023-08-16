T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    for _ in range(K):
        k1, k2 = map(int, input().split())
        arr[k2][k1] = 1

    stack = []
    visited = [[0] * M for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            # 배추를 찾으면
            if arr[i][j] == 1 and visited[i][j] == 0:
                # 방문 표시
                visited[i][j] = 1
                while True:
                    # 방향 배열
                    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < N and 0 <= nj < M:
                            # 방문하지 않은 인접 배추
                            if arr[ni][nj] == 1 and visited[ni][nj] == 0:
                                # 기존 위치 스택에 추가
                                stack.append((i, j))
                                # 위치 변경
                                i, j = ni, nj
                                # 방문 표시
                                visited[i][j] = 1
                                break
                    # 다 돌았는데 방문할 배추가 없다면
                    else:
                        # 돌아가기
                        if stack:
                            i, j = stack.pop()
                        # 돌아갈 곳 없으면 끝
                        else:
                            break
                # 끝났으면 카운트 + 1
                cnt += 1
    print(cnt)
