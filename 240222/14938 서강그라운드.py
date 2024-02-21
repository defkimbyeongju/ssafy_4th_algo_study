from collections import deque
n,m,r = map(int, input().split())
items = [0] + list(map(int, input().split()))
roads = [[]*(n+1) for _ in range(n+1)] # 타겟 노드, 거리 추가
for _ in range(r):
    a,b,c = map(int, input().split())
    roads[a].append((b,c))
    roads[b].append((a,c))

def max_items(num):
    point = items[num]  # 초기 포인트를 시작하는 위치의 item 개수 만큼 주기
    distance = [float('inf') for _ in range(n+1)]
    used = [0] * (n+1)
    used[num] = 1
    q = deque()
    q.append((num, 0)) # 시작 노드, 거리
    while q:
        now, now_dist = q.popleft()
        for next, next_dist in roads[now]:
            d = now_dist+next_dist
            if d > m or distance[next] < d: # 수색 범위보다 더 큰 거리가 나오거나, 이전 기록이 더 짧다면 제끼기
                continue
            distance[next] = d
            if not used[next]: # 이전 방문 기록이 없다면
                point += items[next] # 갈 수 있는 곳이면 point에 추가
                used[next] = 1
            q.append((next, d))
    return point

max_v = 0
for i in range(1,n+1):
    temp = max_items(i)
    max_v = max(temp, max_v)
print(max_v)