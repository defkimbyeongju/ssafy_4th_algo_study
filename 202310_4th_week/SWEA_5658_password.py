def number_maker(nums):
    hex_number = ''
    for i in range(0, N, loop):
        for j in range(loop):
            hex_number += nums[i+j]
        number_set.append(hex_number)
        hex_number = ''


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    numbers = list(input())
    loop = N // 4
    number_set = []
    number_maker(numbers)
    for i in range(loop - 1):
        pop = numbers.pop()
        numbers = [pop] + numbers
        number_maker(numbers)
    number_set = set(number_set)
    number_set = list(number_set)
    ans_list = list(map(lambda x: int(x, 16), number_set))
    ans = sorted(ans_list, reverse=True)[K-1]
    print(f'#{tc} {ans}')
