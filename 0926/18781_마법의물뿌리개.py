T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = list(map(int, input().split()))
    max_t = max(tree)
    tree_c = list(map(lambda x:max_t-x, tree))
    # 가장 키 큰 나무와의 차 리스트

    day = 0
    left = []
    cnt1 = 0

    for c in tree_c:
        if c != 0:
            if c % 2:
                left.append(c-1)
                cnt1 += 1
            else:
                left.append(c)
    # 일단 홀수들은 무조건 1을 한 번 빼야 하므로 걸러내며 cnt1에 개수를 저장

    evensum = sum(left) - cnt1 * 2
    # 남은 짝수들의 합에서 cnt1 개수만큼의 2를 뺐을 때의 값을 저장

    if cnt1 > 0 and evensum < 0:
        day = cnt1 * 2 - 1
        # 이 값이 0보다 작다면 1이 더 많으므로, 1의 개수 * 2 - 1 이 답
    elif evensum == 0:
        day = cnt1 * 2
        # 이 값이 0이라면 1과 2의 개수가 같으므로, 1의 개수 * 2 이 답
    else:
        day = cnt1 * 2
        # 이 값이 0보다 크다면 세트 완성 이후부터 다시 계산

        if evensum % 6 == 0:
            day += (evensum//6) * 4
        elif evensum % 6 == 4:
            day += (evensum//6) * 4 + 3
        elif evensum % 6 == 2:
            day += (evensum//6) * 4 + 2
        # 6을 기준으로 순환하므로

    print(f'#{tc}', day)