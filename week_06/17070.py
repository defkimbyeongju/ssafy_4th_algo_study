# 집의 크기 입력
N = int(input())
# 집의 상태 리스트로 입력
home = [list(map(int, input().split())) for _ in range(N)]
# 해당 칸까지 오는데 가능한 (가로, 대각선, 세로) 경로의 수 리스트 설정
way = [[(0, 0, 0)] * N for _ in range(N)]

# 집을 순회하며 진행
for y in range(N):
    for x in range(1, N):
        # 가장 처음 파이프 위치
        if (y == 0 and x == 0) or (y == 0 and x == 1):
            way[y][x] = (1, 0, 0)
        # 벽이 있는 칸
        elif home[y][x] == 1:
            way[y][x] = (0, 0, 0)
        else:
            # 가로로 오는 경우
            if home[y][x - 1] != 1 and y >= 0 and x - 1 >= 1:
                west = way[y][x - 1][0] + way[y][x - 1][1]
            else:
                west = 0
            # 대각선으로 오는 경우
            if home[y][x - 1] != 1 and home[y - 1][x] != 1 and y - 1 >= 0 and x - 1 >= 1:
                northwest = sum(way[y - 1][x - 1])
            else:
                northwest = 0
            # 세로로 오는 경우
            if home[y - 1][x] != 1 and y - 1 >= 0 and x >= 1:
                north = way[y - 1][x][1] + way[y - 1][x][2]
            else:
                north = 0

            # 현재 위치에 경로의 수 저장
            way[y][x] = (west, northwest, north)

# 마지막 칸으로 이동시키는 방법의 수 출력
print(sum(way[N - 1][N - 1]))
