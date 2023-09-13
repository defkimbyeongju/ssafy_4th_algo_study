import copy
# 중복되니까 절반만
def BFS(start, lst):
    visited = [0] * N
    Q = []
    Q.append(start)
    visited[start] = 1
    while Q:
        now = Q.pop(0)
        for i in range(N):
            if not visited[i] and tmp_arr[now][i] == 1:
                Q.append(i)
                visited[i] = 1
    for i in lst:
        if not visited[i]:
            return False
    return True


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    voters = list(map(int, input().split()))
    towns = list(range(N))
    result = float('inf')
    for i in range(1, 1 << (N - 1)):  # 1<<(N-1) == (1<<N)//2
        area1 = []
        area2 = []
        for j in range(N):
            if i & (1 << j):  # j번 비트가 0이 아니면
                area1.append(towns[j])
            else:
                area2.append(towns[j])
        tmp_arr = copy.deepcopy(arr)
        for n in area1:
            for m in area2:
                tmp_arr[n][m] = 0
                tmp_arr[m][n] = 0
        voter1 = 0
        voter2 = 0
        if BFS(area1[0], area1) and BFS(area2[0], area2):
            for k in area1:
                voter1 += voters[k]
            for l in area2:
                voter2 += voters[l]
            ans = abs(voter1 - voter2)
            if ans < result:
                result = ans
    print(f'#{tc} {result}')
