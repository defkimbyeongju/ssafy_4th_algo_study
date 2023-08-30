T = int(input())
for tc in range(1, T+1):
    N = int(input())
    task = [list(map(int, input().split())) for _ in range(N)]
    task.insert(0, 0)
    ready = [[0] * (N+1) for _ in range(N+1)]
    for i in range(1, N+1):
        if not task[i][1]:
            ready[task[i][1]][i] = 1
        else:
            for j in task[i][2:]:
                ready[j][i] = 1

    min_time = 1000 * N
    for coco in range(1, N+1):

        odd = False
        if task[coco][0] % 2:
            odd = True
        task[coco][0] //= 2

        visited = [False] * (N+1)
        long = [0] * (N+1)
        q = []
        for i in range(1, N+1):
            if ready[0][i]:
                q.append((i, task[i][0]))
        while q:
            n, time = q.pop(0)
            long[n] = time
            visited[n] = True
            for i in range(1, N+1):
                if ready[n][i] and not visited[i]:
                    max_long = 0
                    for r in task[i][2:]:
                        if not visited[r]:
                            break
                        max_long = max(max_long, long[r])
                    else:
                        q.append((i, max_long + task[i][0]))

        if odd:
            task[coco][0] = task[coco][0] * 2 + 1
        else:
            task[coco][0] *= 2

        min_time = min(max(long), min_time)

    if False in visited[1:]:
        min_time = -1
    print(f'#{tc}', min_time)
