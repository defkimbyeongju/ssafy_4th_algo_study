def distance():
    hap = 0
    for y, x in house_list:
        if hap >= ans:
            return hap
        min_dist = 9e9
        for p, q in chicken_list:
            if city[p][q] == 2:
                min_dist = min(min_dist, abs(y - p) + abs(x - q))
        hap += min_dist
    return hap


def closure(level):
    global ans
    if level == close:
        now = distance()
        ans = min(ans, now)
        return
    for r, c in chicken_list:
        if city[r][c] == 2:
            city[r][c] = 0
            closure(level + 1)
            city[r][c] = 2


def distance2(chickens):
    hap = 0
    for y, x in house_list:
        if hap >= ans:
            return hap
        min_dist = 9e9
        for p, q in chickens:
            min_dist = min(min_dist, abs(y - p) + abs(x - q))
        hap += min_dist
    return hap


def closure2(level, lst):
    global ans
    if level == M:
        now = distance2(lst)
        ans = min(ans, now)
        return
    for chicken in chicken_list:
        lst.append(chicken)
        closure2(level + 1, lst)
        lst.pop()


N, M = map(int, input().split())
city = []
house_list = []
chicken_list = []
for i in range(N):
    row = list(map(int, input().split()))
    city.append(row)
    for j in range(N):
        if row[j] == 1:
            house_list.append((i, j))
        elif row[j] == 2:
            chicken_list.append((i, j))
cnt = len(chicken_list)
close = cnt - M
ans = 9e9
if close <= 6:
    closure(0)
else:
    closure2(0, [])
print(ans)
