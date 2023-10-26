def solution(n, computers):
    def find(x):
        if x != parents[x]:
            parents[x] = find(parents[x])
        return parents[x]

    def union(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return
        if x < y:
            parents[y] = x
        else:
            parents[x] = y

    parents = [i for i in range(n)]

    for i in range(n):
        for j in range(n):
            if computers[i][j]:
                union(i, j)

    answer = 0
    for k in range(n):
        if k == parents[k]:
            answer += 1
    return answer