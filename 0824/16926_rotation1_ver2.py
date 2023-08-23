def rotate(k):
    global arr, result
    for j in range(1, N - k * 2):
        result[k + j][k] = arr[k + j - 1][k]
        result[k + j - 1][M - 1 - k] = arr[k + j][M - 1 - k]
    for j in range(1, M - k * 2):
        result[N - 1 - k][i + j] = arr[N - 1 - k][k + j - 1]
        result[k][k + j - 1] = arr[k][k + j]
    for j in range(1, N - k * 2):
        arr[k + j][k] = result[k + j][k]
        arr[k + j - 1][M - 1 - k] = result[k + j - 1][M - 1 - k]
    for j in range(1, M - k * 2):
        arr[N - 1 - k][i + j] = result[N - 1 - k][i + j]
        arr[k][k + j - 1] = result[k][k + j - 1]


N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
result = [[0] * M for _ in range(N)]

for i in range(min(N, M) // 2):
    r = R % ((N - (i * 2 + 1)) * 2 + (M - (i * 2 + 1)) * 2)
    while r > 0:
        rotate(i)
        r -= 1

for x in range(N):
    print(*arr[x])
