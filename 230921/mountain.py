# 다익스트라 알고리즘 적용
# 터널이라는 변수가 있어서 쉽지 않았던 문제입니다.
import heapq
dir = [(0,1),(1,0),(0,-1),(-1,0)] # 상하좌우로 이동 가능
def dijkstra(si,sj):
    distance[si][sj] = 0
    pq = [(0,si,sj)]
    while pq:
        dist, sy, sx = heapq.heappop(pq)
        if distance[sy][sx] < dist: # 현재 좌표의 거리보다 크다면 더 볼 필요 없음
            continue
        # sy,sx가 터널 시작, 끝 점인지 체크
        if_tunnel = tunnel_check(sy,sx)
        if len(if_tunnel) > 0: # 터널에 진입할 수 있다면
            for idx in range(len(if_tunnel)):
                ny, nx, fuel = if_tunnel[idx][0], if_tunnel[idx][1], if_tunnel[idx][2] # 터널의 마지막 부분으로 이동
                new_cost = dist + fuel
                if distance[ny][nx] > new_cost:
                    distance[ny][nx] = new_cost
                    heapq.heappush(pq, (new_cost,ny,nx))
        for y,x in dir: # 무조건 터널을 들어가야 한다는 조건은 없음. 그래서, 터널 진입 여부와 관계 없이 그 위치에서 상하좌우 탐색
            ny, nx = sy+y, sx+x
            if 0<=ny<N and 0<=nx<N:
                # 다음 칸의 높이(더 큼, 같음, 더 작음)에 따라 distance가 달라짐
                if arr[ny][nx] > arr[sy][sx]:
                    new_cost = dist + (arr[ny][nx]-arr[sy][sx])*2
                elif arr[ny][nx] == arr[sy][sx]:
                    new_cost = dist + 1
                else:
                    new_cost = dist
                if distance[ny][nx] > new_cost:
                    distance[ny][nx] = new_cost
                    heapq.heappush(pq,(new_cost,ny,nx))
    return distance[N-1][N-1] # 도착지점 반환

def tunnel_check(i,j): # 터널은 양방향임. 터널의 시작점 or 끝점에 해당하는지 확인하는 함수
    tunnel_start = []
    for idx in range(M):
        if i+1 == tunnel[idx][0] and j+1 == tunnel[idx][1]:
            tunnel_start.append([tunnel[idx][2]-1, tunnel[idx][3]-1, tunnel[idx][4]])
        elif i+1 == tunnel[idx][2] and j+1 == tunnel[idx][3]:
            tunnel_start.append([tunnel[idx][0]-1, tunnel[idx][1]-1, tunnel[idx][4]])
    return tunnel_start


T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    tunnel = [list(map(int, input().split())) for _ in range(M)]
    tunnel.sort(key=lambda x:x[4])
    distance = [[float('inf')]*N for _ in range(N)]
    print(f'#{tc} {dijkstra(0,0)}')