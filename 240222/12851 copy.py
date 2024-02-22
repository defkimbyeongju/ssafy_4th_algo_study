import sys
sys.stdin = open('12851.txt')

from collections import deque

N, K = map(int,input().split())
visited = [0] * 200001

def bfs(n):
    ans_count = 100001
    ans_way = 0

    deq = deque()
    deq.append([n, 0])
    visited[n] = 0

    while deq:
        x, count = deq.popleft()

        if count > ans_count:
            continue

        if x == K:
            if ans_count == 100001:
                ans_count = count

            if count == ans_count:
                ans_way += 1

        arr = [x - 1, x + 1, x * 2]

        for a in arr:
            if 0 <= a <= 200000 and (visited[a] == 0 or visited[a] == count + 1):
                visited[a] = count + 1
                deq.append([a,count + 1])

    return ans_count, ans_way

for ans in bfs(N):
    print(ans)