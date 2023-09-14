def best(st, budget, earn, plus):
    global max_earn, Ms
    if max_earn < earn:
        max_earn = earn
        Ms = budget + plus
    for stock in st:
        if budget - stock[0] >= 0:
            best(st, budget - stock[0], earn + stock[1], plus + stock[2])


T = int(input())
for tc in range(1, T+1):
    Ms, Ma = map(int, input().split())
    Msf = Ms
    N, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for i in range(L):
        max_earn = 0
        lst = []
        for j in range(N):
            if arr[j][i+1] - arr[j][i] > 0:
                lst.append([arr[j][i], arr[j][i+1] - arr[j][i], arr[j][i+1]])
        best(lst, Ms, max_earn, 0)
        Ms += Ma
    print(f'#{tc}', Ms - (Msf + Ma * L))
