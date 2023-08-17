# 학생의 수 입력
N = int(input())

# 학생들 줄 선 순서
student_list = []

# 학생들이 뽑은 번호
number_list = list(map(int, input().split()))

# 뽑은 번호에 따라 줄 서기
for idx in range(len(number_list)):
    student_list.insert(idx - number_list[idx], idx + 1)

# 줄을 선 순서 출력
print(*student_list)
