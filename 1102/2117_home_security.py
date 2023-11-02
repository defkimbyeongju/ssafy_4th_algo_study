# 서비스 영역의 값인 k는 전체 map의 크기인 n보다 클 수 없다.
# 1부터 n까지 k의 값을 설정하고, map의 (0,0)부터 (n-1,n-1)까지 모두 순회하며 이익이 최대가 되는 값을 찾아내겠음(완전탐색)
# 1) 어떤 지점에서 2) 얼만큼의 운영 크기가 최대 이익을 내는지. 2가지를 구해야 한다.
# def security(K, i, j):
#     global max_profit
#     cnt = 0
#     for k in range(K):
#         up, down = i-k, i+k
#         if up == down:
#             for x in range(j-K, j+K):
#                 if 0<=x<N:
#                     if arr[i][x] == 1:
#                         cnt += 1
#         else:
#             for x in range(j, j-K+k, -1): # 왼쪽. 0보다 작으면 break
#                 if x < 0:
#                     break
#                 if up >= 0:
#                     if arr[up][x] == 1:
#                         cnt += 1
#                 if down < N:
#                     if arr[down][x] == 1:
#                         cnt += 1
#             for x in range(j+1, j+K-k): # 오른쪽. N만큼 되면 break
#                 if x >= N:
#                     break
#                 if up >= 0:
#                     if arr[up][x] == 1:
#                         cnt += 1
#                 if down < N:
#                     if arr[down][x] == 1:
#                         cnt += 1
#     temp = (M*cnt) - (K**2 + (K-1)**2)
#     if temp >= 0:
#         max_profit = max(cnt, max_profit)


def security(K, i, j):
    global max_profit
    cnt = 0
    for y in range(N):
        for x in range(N):
            if abs(i-y) + abs(j-x) < K and arr[y][x] == 1:
                cnt += 1
    temp = (M * cnt) - (K ** 2 + (K - 1) ** 2)
    if temp >= 0:
        max_profit = max(cnt, max_profit)


T = int(input())
for tc in range(1,T+1):
    N,M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_profit = 0 # 최대 집 구하기 위한 변수 설정
    for i in range(N):
        for j in range(N):
            for k in range(1,N+2):
                security(k,i,j)
    print(f'#{tc} {max_profit}')