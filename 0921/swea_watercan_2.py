T = int(input())
for tc in range(1, T+1):
    N = int(input())
    H = list(map(int, input().split()))
    max_h = max(H)
    one = two = 0
    for h in H:
        chai = max_h - h
        two += chai // 2
        one += chai % 2
    ans = 0
    if one <= two:
        ans += one * 2
        minus = (two - one) * 2
        if minus % 3 == 0:
            ans += (minus // 3) * 2
        elif minus % 3 == 1:
            ans += (minus // 3) * 2 + 1
        else:
            ans += (minus // 3) * 2 + 2
    else:
        ans += two * 2
        minus = one - two
        ans += minus * 2 - 1
    print(f'#{tc}', ans)