# from collections import deque
# import copy
# # 조합
# def combination(used, n, lst):
#     global max_v
#     if len(lst)==3:
#         arr = copy.deepcopy(lab)
#         for y,x in lst:
#             arr[y][x] = 1
#         res = virus(arr)
#         if res > max_v:
#             max_v = res
#         return
#     for i in range(n,len(used)):
#         if used[i] == 0:
#             used[i] = 1
#             lst.append(safe[i])
#             combination(used, n+1, lst)
#             used[i] = 0
#             lst.pop()
#
#
#
#
# # 바이러스 퍼지기
# def virus(arr):
#     dir = [(0,1),(1,0),(0,-1),(-1,0)]
#     queue = deque()
#     for i in range(N):
#         for j in range(M):
#             if arr[i][j] == 2:
#                 queue.append((i,j))
#     while queue:
#         now_y, now_x = queue.popleft()
#         for y,x in dir:
#             ny, nx = now_y+y, now_x+x
#             if 0<=ny<N and 0<=nx<M and arr[ny][nx] == 0:
#                 arr[ny][nx] = 2
#                 queue.append((ny,nx))
#     arr = sum(arr, [])
#     return arr.count(0)
#
# N,M = map(int,input().split())
# lab = [list(map(int, input().split())) for _ in range(N)]
# safe = [] # 0인 구역
# for i in range(N):
#     for j in range(M):
#         if lab[i][j] == 0:
#             safe.append((i,j))
# used = [0]*len(safe)
# max_v = 0
# combination(used, 0, [])
# print(max_v)

from collections import deque
from itertools import combinations

# 바이러스 퍼지기
def virus(arr):
    dir = [(0,1),(1,0),(0,-1),(-1,0)]
    queue = deque()
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                queue.append((i,j))
    while queue:
        now_y, now_x = queue.popleft()
        for y,x in dir:
            ny, nx = now_y+y, now_x+x
            if 0<=ny<N and 0<=nx<M and arr[ny][nx] == 0:
                arr[ny][nx] = 2
                queue.append((ny,nx))
    count = sum(row.count(0) for row in arr)
    return count

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

# 빈 공간 좌표 저장
empty_spaces = [(i, j) for i in range(N) for j in range(M) if lab[i][j] == 0]

max_v = 0

# 3개의 빈 공간 선택
for combination in combinations(empty_spaces, 3):
    arr = [row[:] for row in lab]  # lab 복사
    for y, x in combination:
        arr[y][x] = 1
    result = virus(arr)
    max_v = max(max_v, result)

print(max_v)
