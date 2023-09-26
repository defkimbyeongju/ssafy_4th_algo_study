T = int(input())
for tc in range(1, T+1):
    N = int(input())
    H = list(map(int, input().split()))
    D = []
    hap = 0
    max_h = max(H)
    for h in H:
        d = max_h - h
        if d == 1:
            D.append(d)
        elif d > 1:
            hap += d
    print(hap, D)
    pre = 0
    for one in range(len(D)):
        if hap - 2 >= 0:
            hap -= 2
            pre += 2
            D.pop()
    if hap % 3 == 0:
        ans = (hap // 3) * 2
        if D:
            ans += len(D) * 2 - 1
    elif hap % 3 == 1:
        ans = (hap // 3) * 2 + 1
        if D:
            ans += len(D) * 2
    else:
        ans = (hap // 3) * 2 + 2
        if len(D) > 1:
            ans += (len(D) - 1) * 2 - 1
    print(f'#{tc}', ans + pre)
