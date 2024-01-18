def get_satisfaction(seats, fav_students, N):
    satisfaction = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for i in range(N):
        for j in range(N):
            student = seats[i][j]
            fav_count = 0
            for dx, dy in directions:
                nx, ny = i + dx, j + dy
                if 0 <= nx < N and 0 <= ny < N and seats[nx][ny] in fav_students[student]:
                    fav_count += 1
            satisfaction += 10 ** (fav_count - 1) if fav_count > 0 else 0
    return satisfaction

def assign_seats(N, student_info):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    seats = [[0 for _ in range(N)] for _ in range(N)]
    fav_students = {student: fav for student, *fav in student_info}
    for student, *fav in student_info:
        best_seat = (-1, -1)
        max_fav_count, max_empty_count = -1, -1
        for r in range(N):
            for c in range(N):
                if seats[r][c] == 0:
                    fav_count, empty_count = 0, 0
                    for dx, dy in directions:
                        nx, ny = r + dx, c + dy
                        if 0 <= nx < N and 0 <= ny < N:
                            if seats[nx][ny] in fav:
                                fav_count += 1
                            elif seats[nx][ny] == 0:
                                empty_count += 1
                    if fav_count > max_fav_count or (fav_count == max_fav_count and empty_count > max_empty_count):
                        max_fav_count, max_empty_count = fav_count, empty_count
                        best_seat = (r, c)
        seats[best_seat[0]][best_seat[1]] = student
    return seats, fav_students

N = int(input())
student_info = [list(map(int, input().split())) for _ in range(N**2)]
seats, fav_students = assign_seats(N, student_info)
satisfaction = get_satisfaction(seats, fav_students, N)
print(satisfaction)