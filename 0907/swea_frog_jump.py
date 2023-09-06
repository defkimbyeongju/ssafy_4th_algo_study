N, Q = map(int, input().split())
wood = []
for _ in range(N):
    x1, x2, y = map(int, input().split())
    wood.append([x2, x1, y])
# wood.sort()
for _ in range(Q):
    s, e = map(int, input().split())
    now = wood[s-1][0]
