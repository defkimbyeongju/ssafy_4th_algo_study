N,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dir = [(0,1),(1,0),(0,-1),(-1,0)]
max_v = -1
used = [[0]*M for _ in range(N)]

def dfs(n,total,lst):
    global max_v
    if n == 4:
        max_v = max(total, max_v)
        return
    for y,x in dir:
        for i,j in lst:
            ny,nx = i+y, j+x
            if 0<=ny<N and 0<=nx<M and not used[ny][nx]:
                used[ny][nx] = 1
                dfs(n+1,total+arr[ny][nx],lst+[[ny,nx]])
                used[ny][nx] = 0
for i in range(N):
    for j in range(M):
        used[i][j] = 1
        dfs(1,arr[i][j],[[i,j]])


# shapes = [[[(0,0),(0,1),(0,2),(0,3)], [(0,0),(1,0),(2,0),(3,0)]],
#           [[(0,0), (0,1), (1,0), (1,1)]],
#           [[(0,0),(1,0),(2,0),(2,-1)],[(0,0),(1,0),(2,0),(2,1)], [(0,0),(0,1),(1,1),(2,1)], [(0,0),(0,-1),(1,-1),(2,-1)]],
#           [[(0,0),(1,0),(1,1),(2,1)],[(0,0),(1,0),(1,-1),(2,-1)], [(0,0),(0,1),(1,1),(1,2)], [(0,0),(0,-1),(1,-1),(1,-2)]],
#           [[(0,0),(0,1),(0,2),(1,1)], [(0,0),(0,1),(0,2),(-1,1)], [(0,0),(1,0),(2,0),(1,1)],[(0,0),(1,0),(2,0),(1,-1)]]]

# for i in range(N):
#     for j in range(M):
#         for i in range(5):
#             for items in shapes[i]:
#                 temp = -1
#                 for y,x in items:
#                     ny, nx = i+y, j+x
#                     if ny <0 or ny>=N or nx < 0 or nx>=M:
#                         break
#                     temp += arr[ny][nx]
#                 else:
#                     max_v = max(temp+1, max_v)
print(max_v)
