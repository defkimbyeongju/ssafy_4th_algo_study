dir = [(-1,-1),(-1,1),(1,1),(1,-1)]
def dfs(si, sj, d, lst):
    global max_v
    if d > 3: return # 가지 치기
    if lst and i == si and j == sj and d == 3:
        max_v = max(max_v, len(lst))
    if arr[i][j] in lst:
        return
    ni, nj = si+dir[d][0], sj+dir[d][1]

    if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] not in lst:
        dfs(ni, nj, d, lst+[arr[ni][nj]]) # 직진
        dfs(ni, nj,d+1,lst+[arr[ni][nj]]) # 회전하는 경우



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = -1
    for i in range(N):
        for j in range(N):
            dfs(i,j,0,[])
    print(f'#{tc} {max_v}')