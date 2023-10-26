def hanoi(n):
    if n == 1:
        return 1
    else:
        return hanoi(n-1) + 2 ** (n-1)

def hanoi_process(n, a, b, c):
    if n == 1:
        print(a, c)
    else:
        hanoi_process(n - 1, a, c, b)
        hanoi_process(1, a, b, c)
        hanoi_process(n - 1, b, a, c)


n = int(input())

if n <= 20:
    print(hanoi(n))
    hanoi_process(n, 1, 2, 3)
else:
    print(hanoi(n))