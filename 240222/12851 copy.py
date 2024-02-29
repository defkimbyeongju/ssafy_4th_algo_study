import sys
sys.stdin = open('12851.txt')

from collections import deque

n, k = map(int,input().split())
way = [0] * 200001

def bfs(n):
    ans_count = 100001
    ans_way = 0

    queue = deque()
    queue.append([n, 0])
    way[n] = 0

    while q:
        x, count = queue.popleft()

        if count > ans_count:
            continue

        if x == k:
            if ans_count == 100001:
                ans_count = count

            if count == ans_count:
                ans_way += 1

        arr = [x - 1, x + 1, x * 2]

        for a in arr:
            if 0 <= a <= 200000 and (way[a] == 0 or way[a] == count + 1):
                                    # 방문을 하지 않았거나, 그 위치에 최단으로 방문한 경우
                way[a] = count + 1
                queue.append([a,count + 1])

    return ans_count, ans_way

result, cnt = bfs(n)