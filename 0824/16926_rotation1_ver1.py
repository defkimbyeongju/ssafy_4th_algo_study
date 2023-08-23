def rotate():
    result = [[0] * M for _ in range(N)]
    for i in range(min(N, M) // 2):
        for j in range(1, N - i * 2):
            result[i + j][i] = arr[i + j - 1][i]
            result[i + j - 1][M - 1 - i] = arr[i + j][M - 1 - i]
        for j in range(1, M - i * 2):
            result[N - 1 - i][i + j] = arr[N - 1 - i][i + j - 1]
            result[i][i + j - 1] = arr[i][i + j]
    return result


N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
while R > 0:
    arr = rotate()
    R -= 1
for k in range(N):
    print(*arr[k])
