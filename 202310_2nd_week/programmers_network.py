def solution(n, computers):
    global parent
    parent = [i for i in range(n)]

    def find(x):
        if parent[x] == x:
            return x
        parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        global parent

        px = find(x)
        py = find(y)

        if px == py:
            return
        if px < py:
            parent[py] = px
        elif px > py:
            parent[px] = py

    for i in range(n):
        for j in range(n):
            # if i == j:
            #     computers[i][j] = 0

            if computers[i][j]:
                union(i, j)

    result = []
    for i in range(n):
        result.append(find(parent[i]))
    result = set(result)
    answer = len(result)

    return answer