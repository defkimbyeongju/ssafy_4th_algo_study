# 하노이 함수 만들기
# n: 원판 개수, start: 시작점, to: 중간점, end: 도착점
def hanoi(n, start, to, end):
    # 원판이 한 개인 경우에는 도착점으로 바로 이동
    if n == 1:
        print(f"{start} {end}")
    # 원판이 한 개 이상일 경우
    else:
        # n-1 개의 원판을 중간점으로 이동시킨 후
        hanoi(n - 1, start, end, to)
        # 가장 큰 원판을 도착점으로 이동시킨 후
        print(f"{start} {end}")
        # 중간점에 있는 n-1 개의 원판을 도착점으로 이동
        hanoi(n - 1, to, start, end)


# 원판의 개수 입력
N = int(input())
# 하노이 탑 이동 횟수 출력
print(2 ** N - 1)
# 하노이 탑 이동 출력
hanoi(N, 1, 2, 3)
