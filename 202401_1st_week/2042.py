# 2042 구간 합 구하기
import sys


def change_num(b, c):
    num_dict[b] = c


def sum_num(b, c):
    total = 0
    for i in range(b, c + 1):
        total += num_dict[i]

    print(total)


# N = 수의 갯수, M = 수 변경 횟수, K = 구간합 구하는 횟수
N, M, K = map(int, sys.stdin.readline().split())

# 숫자들 기록할 dict
num_dict = {}

# 숫자 N개 입력받기
for i in range(N):
    num_dict[i + 1] = int(input())

# 행동 입력받기
for _ in range(M + K):
    A, B, C = map(int, sys.stdin.readline().split())
    if A == 1:
        change_num(B, C)
    else:
        sum_num(B, C)


