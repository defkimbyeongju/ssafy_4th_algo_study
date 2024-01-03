import sys
sys.stdin = open('test.txt')
input = sys.stdin.readline
from collections import deque


# https://yoongrammer.tistory.com/86
# n 명이 학생, m개의 비교
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
in_degree = [0 for _ in range(n+1)]
queue = deque()
T = []

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1

for i in range(1, n+1):
    if in_degree[i] == 0:
        queue.append(i)

while queue:
    now = queue.popleft()
    T.append(now)
    for next in graph[now]:
        in_degree[next] -= 1
        if in_degree[next] == 0:
            queue.append(next)

print(*T)

