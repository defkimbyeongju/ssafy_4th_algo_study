import sys
sys.stdin = open('1525.txt')
input = sys.stdin.readline
from collections import deque
import copy

arr = []

for _ in range(3):
    line = list(map(int, input().split()))
    arr.append(line)


for i in range(3):
    for j in range(3):
        if arr[i][j] == 0:
            sx, sy = i, j
            break


def in_range(x, y):
    if 0<=x<3 and 0<=y<3:
        return True
    return False


# 위, 아래, 왼, 오
def bfs(sx, sy, arr):
    q = deque([(sx, sy, arr, 0, (sx, sy))])
    while q:
        x, y, arr, cnt, prev = q.popleft()
        if arr == [[1, 2, 3],[4, 5, 6],[7, 8, 0]]:
            return cnt
        if arr[x][y] == 0:
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nx, ny = x + dx, y + dy
                if in_range(nx, ny):
                    if (nx, ny) != prev:
                        new_arr = copy.deepcopy(arr)
                        new_arr[x][y], new_arr[nx][ny] = new_arr[nx][ny], new_arr[x][y]
                        q.append((nx, ny, new_arr, cnt+1, (x, y)))

    return -1

result = bfs(sx, sy, arr)

print(result)

'''
2 5 7
8 0 3
4 1 6
답: 18

6 4 7
8 5 0
3 2 1
답 : 31

3 6 0
8 1 2
7 4 5
답 : -1
'''

