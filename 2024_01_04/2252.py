
# def merge(arr):
#     if len(arr) < 2:
#         return arr
    
#     mid = len(arr) // 2
#     left = merge(arr[:mid])
#     right = merge(arr[mid:])
#     return merge_sort(left, right)

# def merge_sort(left, right):
#     i = j = 0
#     result = []

#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

#     if i == len(left):
#         result += right[j:]

#     else:
#         result += left[i:]

#     return result

# arr = [4, 3, 8, 1 , 5, 2, 6, 7]

# array = merge(arr)
# print(array)
    
import sys
from collections import deque

def sort_function():
    result = []
    q = deque()

    # 아무것도 연결되지 않은 것부터 먼저 queue에 입력
    for i in range(1, n + 1):
        if degree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        # 노드와 연결된 간선 제거
        for e in graph[now]:
            degree[e] -= 1
            if degree[e] == 0:
                q.append(e)

    return result

# n : 노드, m : 간선
n, m = map(int, input().split())
degree = [0] * (n + 1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int ,sys.stdin.readline().split())
    graph[a].append(b)
    degree[b] += 1

result = sort_function()
print(*result)



    
