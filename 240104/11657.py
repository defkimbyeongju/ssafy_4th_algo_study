N,M = map(int, input().split())
city = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    city[a].append([b,c])
