# 유저의 수와 친구 관계의 수 입력
N, M = map(int, input().split())
# 친구 관계 입력
friendship_list = [list(map(int, input().split())) for _ in range(M)]

# 각 유저의 케빈 베이컨 수 확인
for n in range(1, N + 1):
    # 다른 각각의 유저들과의 케빈 베이컨 게임 진행
    kevin_bacon_list = [False] * (N + 1)
    # 본인과의 케빈 베이컨 게임 시 0
    kevin_bacon_list[n] = 0
    # 본인을 기점으로 BFS 진행
    queue = [n]

    # BFS 진행
    while queue:
        now = queue.pop(0)
        for friendship in friendship_list:
            if now in friendship:
                now_idx = friendship.index(now)
                following = friendship[not now_idx]

                if kevin_bacon_list[following] is False:
                    queue.append(following)
                    kevin_bacon_list[following] = kevin_bacon_list[now] + 1

    # 전체 인원과의 케빈 베이컨 게임 결과 합을 통한 케빈 베이컨 수 확인
    kevin_bacon_number = sum(kevin_bacon_list)

    # 전체 인원 중에 최소 케빈 베이컨 수 확인
    try:
        if min_kevin_bacon_number > kevin_bacon_number:
            min_kevin_bacon_number = kevin_bacon_number
            min_kevin_bacon_person = n
    except NameError:
        min_kevin_bacon_number = kevin_bacon_number
        min_kevin_bacon_person = n

# 최소 케빈 베이컨 수 출력
print(min_kevin_bacon_person)
