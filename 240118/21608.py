N = int(input())
seats = [[0] * (N) for _ in range(N)]
students = []
for _ in range(N ** 2):
    student = list(map(int, input().split()))
    students.append(student)
    max_point = 0
    max_vacant = 0
    si, sj = 21, 21
    for i in range(N):
        for j in range(N):
            if seats[i][j]:
                continue
            else:
                point = 0
                vacant = 0
                for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < N:
                        if seats[ni][nj] in student[1:]:
                            point += 1
                        elif not seats[ni][nj]:
                            vacant += 1
                if point > max_point:
                    si, sj = i, j
                    max_point = point
                    max_vacant = vacant
                elif point == max_point:
                    if vacant > max_vacant:
                        si, sj = i, j
                        max_vacant = vacant
                    elif vacant == max_vacant:
                        if i < si:
                            si, sj = i, j
                        elif i == si:
                            if j < sj:
                                si, sj = i, j
    seats[si][sj] = student[0]
students.sort()
sati = 0
for y in range(N):
    for x in range(N):
        st = seats[y][x]
        cnt = 0
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N:
                if seats[ny][nx] in students[st - 1][1:]:
                    cnt += 1
        if cnt:
            sati += 10 ** (cnt - 1)
print(sati)