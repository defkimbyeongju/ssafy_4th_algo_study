# dir_odd = [(0,1),(1,0),(0,-1),(-1,0),(1,-1),(1,1)]
# dir_even = [(0,1),(1,0),(0,-1),(-1,0),(-1,-1),(-1,1)]
# def dfs(i,j,v):
#     global result
#     if v==3:
#         total.append(sum(result))
#         return
#     else:
#         if j%2 == 1:
#             for y,x in dir_odd:
#                 nx, ny = i+y, y+j
#                 if -1 < ny < N and -1 < nx < M and check[ny][nx] == 0:
#                     check[ny][nx] = 1
#                     result[v+1] = arr[ny][nx]
#                     dfs(ny,nx,v+1)
#                     check[ny][nx] = 0
#         else:
#             for y,x in dir_even:
#                 nx, ny = i+y, y+j
#                 if -1 < ny < N and -1 < nx < M and check[ny][nx] == 0:
#                     check[ny][nx] = 1
#                     result[v+1] = arr[ny][nx]
#                     dfs(ny,nx,v+1)
#                     check[ny][nx] = 0
#
# T = int(input())
# for tc in range(1,T+1):
#     N,M = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     check = [[0 for _ in range(M)] for _ in range(N)]
#     total = []
#     max_v = 0
#     for i in range(N):
#         for j in range(M):
#             result = [0] * 4
#             result[0] = arr[i][j]
#             check[i][j] = 1
#             dfs(i, j, 0)
#     print(arr)
#     print(f'#{tc} {max(total)}')

dir_odd = [(0,1),(1,0),(0,-1),(-1,0),(1,-1),(1,1)]
dir_even = [(0,1),(1,0),(0,-1),(-1,0),(-1,-1),(-1,1)]
def is_valid_move(i, j, visited, rows, cols):
    return 0 <= i < rows and 0 <= j < cols and not visited[i][j]

def find_combinations(arr):
    rows = len(arr)
    cols = len(arr[0])
    visited = [[False] * cols for _ in range(rows)]

    def backtrack(i, j, path):
        visited[i][j] = True
        path.append(arr[i][j])

        if len(path) == 4:
            combinations.append(list(path))
        else:
            if j%2 == 1:
                for dx, dy in dir_odd:
                    ni, nj = i + dx, j + dy
                    if is_valid_move(ni, nj, visited, rows, cols):
                        backtrack(ni, nj, path)
            else:
                for dx, dy in dir_even:
                    ni, nj = i + dx, j + dy
                    if is_valid_move(ni, nj, visited, rows, cols):
                        backtrack(ni, nj, path)

        visited[i][j] = False
        path.pop()

    combinations = []
    for i in range(rows):
        for j in range(cols):
            backtrack(i, j, [])

    return combinations


T = int(input())
for tc in range(1,T+1):
    N,M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    valid_result = main(arr)
    max_v = 0
    for combination in valid_result:
        if max_v < sum(combination):
            max_v = sum(combination)
    print(f'#{tc} {max_v}')
