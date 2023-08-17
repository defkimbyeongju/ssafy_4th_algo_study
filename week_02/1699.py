# 제곱수들의 합으로 표현할 때의 최소 개수를 구하는 함수
def f(n):
    # f(n)이 이미 계산되지 않은 경우
    if value_list[n] is False:
        # n보다 작거나 같은 수 중에 가장 큰 제곱수의 제곱근
        root = int(n ** (1 / 2))

        # n이 제곱수인 경우
        if n == root ** 2:
            # 제곱수이므로 최소 개수는 한 개가 되고 함수값 리스트에 값 추가
            value_list[n] = 1
            return 1
        # n이 제곱수가 아닌 경우
        else:
            # 최소 개수 변수 설정
            min_counting = 4
            # n보다 작은 제곱수들의 합으로 쪼개기(가장 큰 수부터 확인)
            for m in range(int((n // 2) ** (1 / 2)), root + 1):
                min_counting = min(min_counting, f(m ** 2) + f(n - m ** 2))
            # 최소 개수 파악 후 반환 및 함수값 리스트에 값 추가(개수가 2개인 경우 무조건 최소 개수)
            value_list[n] = min_counting
            return min_counting
    # f(n)이 이미 계산된 경우
    else:
        # 함수값 리스트에서 f(n) 가져오기
        return value_list[n]


# 자연수 입력
N = int(input())
# 함수값 리스트 설정(그대로 인덱스 사용하기 위해 N+1 칸 리스트 설정)
value_list = [False] * (N + 1)

# 출력
print(f(N))
