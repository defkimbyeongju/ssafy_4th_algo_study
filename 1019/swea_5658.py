T = int(input())
hexa = {'0': 0, '1': 1, '2': 2, '3': 3,
        '4': 4, '5': 5, '6': 6, '7': 7,
        '8': 8, '9': 9, 'A': 10, 'B': 11,
        'C': 12, 'D': 13, 'E': 14, 'F': 15}
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(input())
    nums = set()
    length = N // 4
    for _ in range(length):
        for k in range(0, N, length):
            n = 0
            for i in range(length):
                n += (16 ** (length - 1 - i)) * hexa[arr[k + i]]
            nums.add(n)
        arr.insert(0, arr.pop())
    nums_list = list(nums)
    nums_list.sort(reverse=True)
    print(f'#{tc}', nums_list[K - 1])