def tree_water(trees, N):
    days = 0  # 초기 날짜는 0으로 설정
    while True:
        days += 1  # 하루가 지나감
        temp = 1 if days % 2 == 1 else 2  # 홀수날이면 1, 짝수날이면 2
        for i in range(1, N):  # 1부터 N-1까지
            if trees[i] < trees[0] - 2:  # 현재 나무의 높이가 최댓값과 2 이상 차이나면
                trees[i] += temp  # 현재 나무에 물을 주고
                break # 여기서 물을 줬으니 하루를 추가해야 됨
            elif trees[i] < trees[0]:  # 현재 나무의 높이가 최댓값과 2 이하 차이면
                if trees[0] - trees[i] == temp:
                    trees[i] += temp  # 현재 나무에 물을 주고
                    break  # 여기서 물을 줬으니 하루를 추가해야 됨
        if sum(trees) == trees[0] * N:
            break
    return days

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    trees = list(map(int,input().split()))
    trees.sort(reverse=True)
    if sum(trees) == trees[0] * N:
        result = 0
    else:
        result = tree_water(trees,N)
    print(f'#{tc} {result}')
