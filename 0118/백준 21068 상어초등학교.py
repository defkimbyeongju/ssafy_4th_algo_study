N = int(input())
arr = [[0]*N for _ in range(N)]
likes = [[] for _ in range(((N**2)+1))]
dir = [(0,1),(0,-1),(-1,0),(1,0)]
def positioning(idx):
    lst = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                continue
            count = 0
            empty = 0
            for y,x in dir:
                ny, nx = i+y, x+j
                if 0<=ny<N and 0<=nx<N:
                    if arr[ny][nx] in likes[idx]:
                        count += 1
                    elif arr[ny][nx] == 0:
                        empty += 1
            if len(lst) == 0:
                lst.append((count,empty,i,j))
                continue
            if lst[0][0] < count:
                lst.pop()
                lst.append((count, empty, i, j))
                continue
            elif lst[0][0] > count:
                continue
            if lst[0][1] < empty:
                lst.pop()
                lst.append((count, empty, i, j))
                continue
            elif lst[0][1] > empty:
                continue
            if lst[0][2] > i:
                lst.pop()
                lst.append((count, empty, i, j))
                continue
            elif lst[0][2] < i:
                continue
            if lst[0][3] > j:
                lst.pop()
                lst.append((count, empty, i, j))
                continue
    return (lst[0][2], lst[0][3])

for i in range(N**2):
    idx, a, b, c, d = map(int, input().split())
    likes[idx].append(a)
    likes[idx].append(b)
    likes[idx].append(c)
    likes[idx].append(d)
    y,x = positioning(idx)
    arr[y][x] = idx
result = 0
points = [0,1,10,100,1000]
for i in range(N):
    for j in range(N):
        count = 0
        for y,x in dir:
            ny, nx = i+y, j+x
            if 0<=ny<N and 0<=nx<N:
                if arr[ny][nx] in likes[arr[i][j]]:
                    count += 1
        result += points[count]
print(result)
