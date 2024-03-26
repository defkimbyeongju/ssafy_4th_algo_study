from collections import deque

N, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = float('-infinity')

def dfs(near, has_used, profit, y, x):
    global answer

    profit += arr[y][x]

    if (y, x) == (N - 1, N - 1):
        answer = max(answer, profit)
        return
    
    if not has_used:
        temp = near.copy()
        temp.append((y, x))
        if len(temp) > T:
            ny, nx = temp.popleft()
            dfs(0, True, profit, ny, nx)
        for dy, dx in [(1, 0), (0, 1)]:
            ny, nx = y + dy, x + dx
            if ny < N and nx < N:
                dfs(temp, has_used, profit, ny, nx)
    else:
        for dy, dx in [(1, 0), (0, 1)]:
            ny, nx = y + dy, x + dx
            if ny < N and nx < N:
                dfs(near, has_used, profit, ny, nx)

dfs(deque(), False, 0, 0, 0)
print(answer)