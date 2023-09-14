# 백준 16926 배열 돌리기
N,M,R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
mini = min(N,M)//2  # 행의 개수 N, 열의 개수 M 중 더 작은 값을 2로 나눈 몫만큼 바퀴를 돌면서 배열을 돌림
for _ in range(R):
    for i in range(mini):
        x, y = i, i
        temp = arr[x][y] # 다음 배열에 옮길 값 지정
        for j in range(i+1, N-i): # 좌. 가장 바깥에 위치한 배열들부터 시작하기
            x = j
            prev_value = arr[x][y] # 다른 값으로 대체되기 전에 변수로 저장
            arr[x][y] = temp # 값 변경
            temp = prev_value # 이전에 있던 값이 이제는 다음 배열에 들어갈 값이 된다
        for k in range(i+1, M-i): # 하
            y = k
            prev_value = arr[x][y]
            arr[x][y] = temp
            temp = prev_value
        for l in range(i+1, N-i): # 우
            x = N-l-1
            prev_value = arr[x][y]
            arr[x][y] = temp
            temp = prev_value
        for m in range(i+1, M-i): # 상
            y = M-m-1
            prev_value = arr[x][y]
            arr[x][y] = temp
            temp = prev_value
for i in range(N):
    for j in range(M):
        print(arr[i][j], end=' ')
    print()
