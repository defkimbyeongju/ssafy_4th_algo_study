# 전체 사람의 수 입력
N = int(input())
# 촌수를 계산해야 하는 서로 다른 두 사람의 번호 입력
n1, n2 = map(int, input().split())
# 부모 자식들 간의 관계의 개수 입력
M = int(input())

# 친척 관계 입력받아 리스트에 저장
relative_list = [list(map(int, input().split())) for _ in range(M)]
# 촌수 저장할 리스트 생성
chon_list = [False] * (N + 1)
# 첫째 사람에 대하여 BFS 진행
queue = [n1]
# 자기 자신은 촌수 0 저장
chon_list[n1] = 0

# BFS 진행
while queue:
    now = queue.pop(0)
    for relative in relative_list:
        if now in relative:
            now_idx = relative.index(now)
            following = relative[not now_idx]
            if chon_list[following] is False:
                queue.append(following)
                chon_list[following] += chon_list[now] + 1

# 촌수 출력
if chon_list[n2]:
    print(chon_list[n2])
else:
    print(-1)
