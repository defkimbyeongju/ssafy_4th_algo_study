from collections import deque
import sys

input = sys.stdin.readline
N, K = map(int, input().split())
queue = deque()
queue.append(N)
visited = [0] * 100001
cnt, result = 0, 0
while queue:
    curr = queue.popleft()
    temp = visited[curr]
    if curr == K:
        result = temp
        cnt += 1
        continue

    for nxt_num in [curr - 1, curr + 1, curr * 2]:
        if 0 <= nxt_num < 100001 and (
            visited[nxt_num] == 0 or visited[nxt_num] == visited[curr] + 1
        ):
            visited[nxt_num] = visited[curr] + 1
            queue.append(nxt_num)
print(result)
print(cnt)
