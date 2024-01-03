import sys

v, m = map(int, input().split())

dis = [1e9] * (v + 1)
graph = []
start = 1e9

for _ in range(m):
    s, e, weight = map(int, sys.stdin.readline().split())
    graph.append([s,e,weight])
    if start > s:
        start = s

def ballmanford(start):
    dis[start] = 0

    # v번 반복해서 싸이클이 생기는지 확인
    for i in range(v):
        # e개의 간선을 이동
        for j in range(m):
            cur, nxt, weight = graph[j]
            if dis[cur] + weight < dis[nxt]:
                dis[nxt] = dis[cur] + weight

                if i == v - 1:
                    return False

    return True

if start != 1:
    for _ in range(v-1):
        print("-1")
else:
    if ballmanford(1):
        for i in range(2, v+1):
            if dis[i] == 1e9:
                print("-1")
            else:
                print(dis[i])
    else:
        print("-1")