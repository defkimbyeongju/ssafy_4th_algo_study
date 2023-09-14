def pipe(i, j, status):
    global cnt
    if i == N - 1 and j == N - 1:
        cnt += 1
        return
    if status == 1 or status == 3:
        if j + 1 < N and arr[i][j + 1] == 0:
            pipe(i, j + 1, 1)

    if status == 2 or status == 3:
        if i + 1 < N and arr[i + 1][j] == 0:
            pipe(i + 1, j, 2)

    if i + 1 < N and j + 1 < N:
        if arr[i][j + 1] == 0 and arr[i + 1][j + 1] == 0 and arr[i + 1][j] == 0:
            pipe(i + 1, j + 1, 3)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
# 가로: 1, 세로: 2, 대각선: 3
pipe(0, 1, 1)
print(cnt)
