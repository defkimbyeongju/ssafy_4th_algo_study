# short = [int(input()) for _ in range(9)]
#
# for i in range(1<<9):
#     seven = []
#     for j in range(9):
#         if i & (1<<j):
#             seven.append(short[j])
#     if len(seven) == 7 and sum(seven) == 100:
#         break
#
# for i in sorted(seven):
#     print(i)

# n = int(input())
# cnt = 1
# if n == 1:
#     cnt = 0
# while n > 3:
#     if n % 3 == 0:
#         n /= 3
#     elif n % 2 == 0:
#         if (n-1) % 3 == 0:
#             n -= 1
#     else:
#         n -= 1
#     cnt += 1
#
# print(cnt)

# 백준 1932 정수삼각형

# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]
# dp = [[0]*N for _ in range(N+1)]
#
# for i in range(1,N+1): # i, i+1


# 백준 2839 설탕 배달

# n = int(input())
# def sugar(n):
#     dp = [0]*(n+1)
#     dp[3] = 1
#     dp[4] = -1
#     dp[5] = 1
#     dp[6] = 2
#     dp[7] = -1
#     dp[8] = 2
#     if n > 9:
#         for i in range(9, n+1):
#             if dp[i-3] == -1 and dp[i-5] == -1:
#                 dp[i] = -1
#             elif dp[i-3] == -1 and dp[i-5] != -1:
#                 dp[i] = dp[i-5]+1
#             elif dp[i-3] != -1 and dp[i-5] == -1:
#                 dp[i] = dp[i-3]+1
#             else:
#                 dp[i] = min(dp[i-3], dp[i-5])+1
#
#     return dp[n]
#
# print(sugar(n))


# 백준 1389 케빈 베이컨

# def bfs(s,g):
#     queue = []
#     visited = [0]*(N+1)
#     queue.append(s)
#     visited[s] = 1
#     while queue:
#         t = queue.pop(0)
#         if t == g:
#             return visited[t]-1
#         for i in arr[t]:
#             if visited[i] == 0:
#                 visited[i] = visited[t]+1
#                 queue.append(i)
#
# N,M = map(int, input().split())
# arr = [[] for _ in range(N+1)]
# for _ in range(M):
#     a,b = map(int, input().split())
#     arr[a].append(b)
#     arr[b].append(a)
# min_v = 21e8
# for i in range(1,N+1):
#     total = 0
#     for j in range(1, N+1):
#         total += bfs(i, j)
#     if min_v > total:
#         min_v = total
#         minimum = [i]
#     elif min_v == total:
#         minimum.append(i)
#
# print(minimum[0])


# 백준 7576 토마토
# def bfs(queue):
#     dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#     while queue:
#         i, j = queue.popleft()
#         for y, x in dir:
#             ny, nx = y+i, x+j
#             if 0<=ny<N and 0<=nx<M:
#                 if arr[ny][nx] == 0:
#                     arr[ny][nx] = 1
#                     visited[ny][nx] = visited[i][j] + 1
#                     queue.append((ny,nx))
#
# from collections import deque
# M,N = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
# queue = deque()
# visited = [[0]*M for _ in range(N)]
#
# if 0 not in sum(arr, []):
#     result = 0
# else:
#     for i in range(N):
#         for j in range(M):
#             if arr[i][j] == 1:
#                 queue.append((i,j))
#                 visited[i][j] = 1
#     bfs(queue)
#     if 0 in sum(arr,[]):
#         result = -1
#     else:
#         result = max(sum(visited, []))-1
#
# print(result)

# 백준 16926 배열돌리기1

N,M,R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
mini = min(N,M)//2

for _ in range(R):
    for i in range(mini):
        x, y = i, i
        temp = arr[x][y]
        for j in range(i+1, N-i): # 좌
            x = j
            prev_value = arr[x][y]
            arr[x][y] = temp
            temp = prev_value
        for k in range(i+1, M-i): # 하
            y = k
            prev_value = arr[x][y]
            arr[x][y] = temp
            temp = prev_value
        for l in range(i+1, N-i): # 우
            x = N-l-1
            prev_value = arr[x][y]
            arr[x][y] = temp
            temp = prev_value
        for m in range(i+1, M-i): # 상
            y = M-m-1
            prev_value = arr[x][y]
            arr[x][y] = temp
            temp = prev_value
for i in range(N):
    for j in range(M):
        print(arr[i][j], end=' ')
    print()
