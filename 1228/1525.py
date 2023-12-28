from collections import deque
target = '123456780'
start = ''
for _ in range(3):
    a = input()
    start += a.replace(" ", "")

dir = [(0,1),(1,0),(0,-1),(-1,0)]

check = {start:0}
q = deque([start])

def bfs():
    while q:
        now = q.popleft()
        idx = now.index('0')
        cnt = check[now]
        y,x = idx//3, idx%3
        if now == target:
            return cnt
        for i,j in dir:
            ny, nx = y+i, x+j
            if 0<=ny<3 and 0<=nx<3:
                next = list(now)
                change = ny*3+nx%3
                next[change], next[idx] = next[idx], next[change]
                next = "".join(next)
                if check.get(next, 0) == 0:
                    check[next] = cnt+1
                    q.append(next)
    return -1

print(bfs())

