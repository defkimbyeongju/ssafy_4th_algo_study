# 문제

# N개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 버스가 M개 있다. 각 버스는 A, B, C로 나타낼 수 있는데, A는 시작도시, B는 도착도시, C는 버스를 타고 이동하는데 걸리는 시간이다. 시간 C가 양수가 아닌 경우가 있다. C = 0인 경우는 순간 이동을 하는 경우, C < 0인 경우는 타임머신으로 시간을 되돌아가는 경우이다.

# 1번 도시에서 출발해서 나머지 도시로 가는 가장 빠른 시간을 구하는 프로그램을 작성하시오.
# 입력

# 첫째 줄에 도시의 개수 N (1 ≤ N ≤ 500), 버스 노선의 개수 M (1 ≤ M ≤ 6,000)이 주어진다. 둘째 줄부터 M개의 줄에는 버스 노선의 정보 A, B, C (1 ≤ A, B ≤ N, -10,000 ≤ C ≤ 10,000)가 주어진다. 
# 출력

# 만약 1번 도시에서 출발해 어떤 도시로 가는 과정에서 시간을 무한히 오래 전으로 되돌릴 수 있다면 첫째 줄에 -1을 출력한다. 그렇지 않다면 N-1개 줄에 걸쳐 각 줄에 1번 도시에서 출발해 2번 도시, 3번 도시, ..., N번 도시로 가는 가장 빠른 시간을 순서대로 출력한다. 만약 해당 도시로 가는 경로가 없다면 대신 -1을 출력한다.

# 벨만-포드 알고리즘
# 1. 모든 엣지와 관련된 정보를 가저온 후 다음 조건에 따라 거리 리스트의 값을 업데이트
# 	- 출발 노드가 방문한 적이 없는 노드일 때 값을 업데이트하지 않는다.
# 	- 출발 노드의 거리 리스트값 + 엣지 가중치 < 종료 노드의 거리 리스트 값일 때 종료 노드의 거리 리스트 업데이트
# 2. 노드 개수 -1번만큼 1을 반복
# 3. 음수 사이클 유무를 알기 위해 모든 엣지에 대해 다시 한번 1을 수행한다. 
# 	- 한 번이라도 값이 업데이트 되면 음수 사이클이 존재한다고 판단

import sys
input = sys.stdin.readline
INF = float('inf')

v, e = map(int, input().split())    # 노드의 개수, 간선의 개수
edges = []                          # 1. 모든 간선에 대한 정보를 담는 리스트
distance = [INF] * (v + 1)          # 최단 거리 테이블을 모두 무한으로 초기화

# 모든 간선의 정보 입력
for _ in range(e):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미 (a -> b 의 비용이 c)
    edges.append((a, b, c))


def bellman_ford(start):
    # 1-1. 출발 노드는 0으로(자기자신까지의 거리는 0)
    distance[start] = 0
    # 2. 모든 엣지를 확인해 리스트 업데이트
    for i in range(v):
        # 매 반복마다 '모든 간선'을 확인한다.
        # 2-1. 음수 사이클이 없을 때 특정 노드의 최단거리를 구성할 수 있는 엣지의 최대 개수는 노드개수-1 
        for j in range(e):
            cur_node = edges[j][0]
            next_node = edges[j][1]
            edge_cost = edges[j][2]
            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if distance[cur_node] != INF and distance[next_node] > distance[cur_node] + edge_cost:
                distance[next_node] = distance[cur_node] + edge_cost
                # 3. v번째 라운드에서도 값이 갱신된다면 음수 순환이 존재
                if i == v - 1:
                    return True

    return False


# 시작 노드는 1
negative_cycle = bellman_ford(1)

# 음수 순환이 존재
if negative_cycle:
    print("-1")
else:
    # 1번 노드를 제외한 다른 모든 노드로 가기 위한 최단 거리를 출력
    for i in range(2, v + 1):
        # 도달할 수 없는 경우, -1 출력
        if distance[i] == INF:
            print("-1")
        # 도달할 수 있으면 거리 출력
        else:
            print(distance[i])
