def DFS(y, x, arr):     # 각 배추군락의 배추를 모두 뽑아버리는 DFS 함수
    stack = []          # 빈 스택 생성
    arr[y][x] = 0       # 해당 배추 뽑기
    direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # 배추군락은 상하좌우로 연결되어야 함
    while True:         
        for dy, dx in direction:        
            ny, nx = y + dy, x + dx         # 해당 배추를 기준으로 상하좌우 방향을 탐색
            if 0 <= ny < N and 0 <= nx < M: # 범위가 배추밭을 넘어가지 않는 선에서
                if arr[ny][nx] == 1:        # 만약 이동할 배추가 있다면,
                    stack.append((y, x))    # 기존 배추좌표는 저장
                    y, x = ny, nx           # 배추이동
                    arr[y][x] = 0           # 이동한 뒤 배추뽑기!
                    break
        else:
            if stack:                       # 근처에 더 뽑을 배추가 없다면
                y, x = stack.pop()          # 다시 전 위치로 돌아가서 탐색
            else:
                break                       # 아예 배추군락지의 배추를 다 뽑았으면
                                            # 해당 좌표에서의 배추군락 정리는 완료
    return 1       # 이 함수가 한번 작동할 때마다 배추군락이 하나 정리되므로 1을 리턴
                                        

T = int(input())
for tc in range(T):
    M, N, K = map(int, input().split())
    ground = [[0] * M for _ in range(N)]    # 빈 배추밭 생성
    for _ in range(K):
        x, y = map(int, input().split())
        ground[y][x] = 1                    # 좌표입력받아 배추심기

    cnt = 0                                 # 배추군락지 개수를 셀 변수 선언
    for i in range(N):
        for j in range(M):                  # 배추밭을 순회하면서,
            if ground[i][j] == 1:           # 배추가 심겨있다면,
                cnt += DFS(i, j, ground)    # 해당 배추군락의 배추를 모두 뽑아버리고
                                            # 1을 리턴 받아 cnt에 합산
    print(cnt)      # 결과 출력
