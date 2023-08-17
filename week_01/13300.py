# 학생 수, 최대 인원 수 입력
N, K = map(int, input().split())

# 방 리스트 만들기
student_list = [0] * 12

# 각 성별, 학년 입력에 대하여 방 배정
for _ in range(N):
    # 성별, 학년 입력
    sex, year = map(int, input().split())

    # 인원 수 파악
    student_list[(year - 1) * 2 + sex] += 1

# 방 개수 계산 및 출력
room = 0
for idx in range(12):
    room += (student_list[idx] // K) + int(bool(student_list[idx] % K))

print(room)
