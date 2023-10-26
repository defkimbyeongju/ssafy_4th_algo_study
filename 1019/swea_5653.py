T = int(input())
for tc in range(1, T+1):
    M, A = map(int, input().split())
    move_a = list(map(int, input().split()))
    move_b = list(map(int, input().split()))
    arr = [[0] * 11 for _ in range(11)]
    powers = [0] * A
    for i in range(A):
        y, x, c, p = map(int, input().split())
        powers[i] = p
