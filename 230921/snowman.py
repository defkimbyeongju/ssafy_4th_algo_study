def dfs(i,j,gage):
    if arr[i][j] == 3:
        result.append(gage)
        return
    if j-1 > 0 and arr[i][j-1] == 1 and visited[i][j-1] == 0:
        dfs(i, j-1, gage)
    elif j+1 < M and arr[i][j+1] == 1 and visited[i][j+1] == 0:
        dfs(i, j+1, gage)
    if i == 0: # 스노우맨이 제일 위에 있을 때
        for k in range(i+1,N):
            if arr[k][j] == 1 and visited[k][j] == 0:
                dfs(k, j, gage+k)
    elif i == N-1: # 스노우맨이 제일 아래에 있을 때
        for k in range(i, -1, -1):
            if arr[k][j] == 1 and visited[k][j] == 0:
                dfs(k, j, gage+(i-k))
    else: # 스노우맨이 중간에 있을 때
        for k in range(i): # 위에서부터 순회 한 번
            if arr[k][j] == 1 and visited[k][j] == 0:
                dfs(k, j, gage+(i-k))
        for k in range(i+1, N-1):
            if arr[k][j] == 1 and visited[k][j] == 0:
                dfs(k, j, gage+)