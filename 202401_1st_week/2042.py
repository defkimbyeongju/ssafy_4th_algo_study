# 2042 구간 합 구하기

# N = 수의 갯수, M = 수 변경 횟수, K = 구간합 구하는 횟수
N, M, K = map(int, input().split())

# 숫자들 기록할 dict
num_dict = {}

# 숫자 N개 입력받기
for i in range(N):
    num_dict[i + 1] = int(input())

print(num_dict)


