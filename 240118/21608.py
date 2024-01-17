N = int(input())
seats = [[0] * (N) for _ in range(N)]
print(seats)
for _ in range(N ** 2):
    student = list(map(int, input().split()))
    nominee = []
    for i in range(N):
        for j in range(N):
            if seats[i][j]:
                continue
            else:
                for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    ni, nj = i + di, j + dj
                    