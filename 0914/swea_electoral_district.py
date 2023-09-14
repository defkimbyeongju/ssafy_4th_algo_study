def f():
    global min_chai
    B = list(set(All) - set(A))
    check1 = check2 = True
    for a1 in range(len(A) - 1):
        for a2 in range(a1 + 1, len(A)):
            check1 = bfs(A[a1], A[a2], A)
            if not check1:
                break
        if not check1:
            break
    for b1 in range(len(B) - 1):
        for b2 in range(b1 + 1, len(B)):
            check2 = bfs(B[b1], B[b2], B)
            if not check2:
                break
        if not check2:
            break
    if check1 and check2:
        hap1 = hap2 = 0
        for a in A:
            hap1 += population[a]
        for b in B:
            hap2 += population[b]
        chai = abs(hap1 - hap2)
        min_chai = min(min_chai, chai)
    if len(A) == N-1:
        return
    else:
        for j in range(max(A)+1, N):
            A.append(j)
            f()
            A.pop()


def bfs(y, x, dist):
    visited = [0] * N
    visited[y] = 1
    q = [y]
    while q:
        t = q.pop(0)
        if t == x:
            return True
        else:
            for i in range(N):
                if arr[t][i] and not visited[i] and i in dist:
                    q.append(i)
                    visited[i] = 1
    return False


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    population = list(map(int, input().split()))
    min_chai = 20 ** 2
    All = [i for i in range(N)]
    A = [0]
    f()
    print(f'#{tc}', min_chai)
