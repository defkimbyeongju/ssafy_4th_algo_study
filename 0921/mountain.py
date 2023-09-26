# 다익스트라 알고리즘 활용
# 터널이 관건임
# 처음에 헤맸던 이유: 1) 터널의 끝점은 다루지 않고, 시작점만 체크함. 2) 터널 안의 좌표들은 어떻게 처리해야 하나..? 3) 터널에 도달해도, 터널을 통과하는게 더 비효율적일 수 있다면 원래대로 가는게 더 낫지 않을까?
import heapq
dir = [(0,1),(1,0),(0,-1),(-1,0)]
def dijkstra(si,sj):
    distance[si][sj] = 0 # 2차원 배열로 distance 생성
    pq = [(0,si,sj)] # 우선순위 큐
    while pq:
        dist, sy, sx = heapq.heappop(pq)
        if distance[sy][sx] < dist:
            continue
        # sy,sx가 터널 시작점, 끝점인지 체크
        if_tunnel = tunnel_check(sy,sx)
        if len(if_tunnel) > 0: # 해당 좌표에서 터널이 존재한다면
            for idx in range(len(if_tunnel)): # ny,nx를 터널의 반대편으로 설정하고 다익스트라 알고리즘 구현
                ny, nx, fuel = if_tunnel[idx][0], if_tunnel[idx][1], if_tunnel[idx][2]
                new_cost = dist + fuel
                if distance[ny][nx] > new_cost:
                    distance[ny][nx] = new_cost
                    heapq.heappush(pq, (new_cost,ny,nx))
        for y,x in dir: # 상하좌우 방향 배열로 돌아다니며 distance 최신화
            ny, nx = sy+y, sx+x
            if 0<=ny<N and 0<=nx<N:
                # 다음 칸의 높이(더 큼, 같음, 더 작음)에 따라 distance가 달라짐
                if arr[ny][nx] > arr[sy][sx]: # 다음 칸의 높이가 더 크다면
                    new_cost = dist + (arr[ny][nx]-arr[sy][sx])*2
                elif arr[ny][nx] == arr[sy][sx]: # 다음 칸과 높이가 같다면
                    new_cost = dist + 1
                else: # 다음 칸의 높이가 현재보다 낮다면
                    new_cost = dist
                if distance[ny][nx] > new_cost:
                    distance[ny][nx] = new_cost
                    heapq.heappush(pq,(new_cost,ny,nx))
    return distance[N-1][N-1]

def tunnel_check(i,j): # 터널은 양방향으로 오고 갈 수 있음
    tunnel_start = [] # 한 점에서 시작하는 터널이 여러 개일 수 있기 때문에 해당 좌표에 해당하는 터널 지점을 리스트에 담음
    for idx in range(M):
        if i+1 == tunnel[idx][0] and j+1 == tunnel[idx][1]: # 터널의 시작점에 해당하는지 확인
            tunnel_start.append([tunnel[idx][2]-1, tunnel[idx][3]-1, tunnel[idx][4]])
        elif i+1 == tunnel[idx][2] and j+1 == tunnel[idx][3]: # 터널의 끝점에 해당하는지 확인
            tunnel_start.append([tunnel[idx][0]-1, tunnel[idx][1]-1, tunnel[idx][4]])
    return tunnel_start


T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    tunnel = [list(map(int, input().split())) for _ in range(M)]
    tunnel.sort(key=lambda x:x[4]) # 혹시라도 시간을 좀 더 줄일 수 있을까봐 연료 소모량 순으로 터널 정렬
    distance = [[float('inf')]*N for _ in range(N)]
    print(f'#{tc} {dijkstra(0,0)}')