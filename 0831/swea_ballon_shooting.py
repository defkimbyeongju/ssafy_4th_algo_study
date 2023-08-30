def f(i, n, order):
    global max_point
    if i == n:
        point = 0
        balloon2 = balloon[:]
        order2 = order[:]
        for k in order2:
            if len(balloon2) == 2:
                point += max(balloon2) * 2
                break
            elif len(balloon2) == 1:
                point += balloon2[0]
            elif k == 0:
                point += balloon2[k + 1]
                balloon2.pop(k)
            elif k == len(balloon2) - 1:
                point += balloon2[k - 1]
                balloon2.pop(k)
            else:
                point += balloon2[k - 1] * balloon2[k + 1]
                balloon2.pop(k)
            for p in range(len(order2)):
                if order2[p] > k:
                    order2[p] -= 1
        if max_point < point:
            max_point = point
    else:
        for j in range(i, n):
            order[i], order[j] = order[j], order[i]
            f(i+1, n, order)
            order[i], order[j] = order[j], order[i]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    balloon = list(map(int, input().split()))

    order1 = [i for i in range(N)]
    max_point = 0
    f(0, N, order1)
    print(f'#{tc}', max_point)
