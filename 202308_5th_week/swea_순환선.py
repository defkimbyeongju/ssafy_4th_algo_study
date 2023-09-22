def f(i, N, K):     # i 이전에 고른 개수, N개에서 K개를 고르는 순열
    global max_v
    if i == K:      # 순열 완성 : K개를 모두 고른 경우
        for n in range(len(p)-1):
            for m in range(n+1, len(p)):
                # 서로 붙어 있는 역이면 pass
                if abs(p[n] - p[m]) < 2 or abs(p[n] - p[m]) == 9:
                    return
        else:   # 노선이 서로 교차하지 않도록 섹터를 나누기
            if p[0] < p[1]:
                lst1 = list(range(p[0] + 1, p[1]))
                lst2 = list(range(p[1] + 1, N+1))
                lst2.append(list(range(0, p[0])))
            else:
                lst1 = list(range(p[0], p[1], -1))
                lst2 = list(range(p[0] + 1, N + 1))
                lst2.append(list(range(0, p[1])))
                # 새로운 노선이 교차하지 않는(동일한 섹터 내에) 다면
            if (p[2] in lst1 and p[3] in lst1) or (p[2] in lst2 and p[3] in lst2):
                ans = (passenger[p[0]]+passenger[p[1]])**2 + (passenger[p[2]]+passenger[p[3]])**2
                if max_v < ans:
                    max_v = ans
                return

    else:   # p[i]에 들어갈 숫자를 결정
        for j in range(N):
            if used[j] == 0:    # 아직 사용되기 전이면
                p[i] = station[j]
                used[j] = 1
                f(i+1, N, K)
                used[j] = 0


T = int(input())    # 테스트 케이스 수
for tc in range(1, T+1):
    N = int(input())    # 지하철 역 수
    passenger = list(map(int, input().split()))   # 역 별 지하철 승객 수
    station = list(range(N))
    used = [0] * N
    p = [0] * 4
    max_v = 0
    f(0, N, 4)
    print(f'#{tc} {max_v}')
