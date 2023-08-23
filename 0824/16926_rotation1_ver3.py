N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

for k in range(min(N, M) // 2):
    r = R % ((N - (k * 2 + 1)) * 2 + (M - (k * 2 + 1)) * 2)
    while r > 0:
        prev1 = arr[k][k]
        prev2 = arr[N - (k + 1)][M - (k + 1)]
        for j in range(1, N - k * 2):
            temp1 = arr[k + j][k]
            arr[k + j][k] = prev1
            prev1 = temp1

            temp2 = arr[N - j - (k + 1)][M - 1 - k]
            arr[N - j - (k + 1)][M - 1 - k] = prev2
            prev2 = temp2

        for j in range(1, M - k * 2):
            temp1 = arr[N - 1 - k][k + j]
            arr[N - 1 - k][k + j] = prev1
            prev1 = temp1

            temp2 = arr[k][M - (k + j + 1)]
            arr[k][M - (k + j + 1)] = prev2
            prev2 = temp2

        r -= 1

for x in range(N):
    print(*arr[x])
