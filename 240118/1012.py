from collections import deque
T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    answer = 0
    baechoos = [list(map(int, input().split())) for _ in range(K)]
    while baechoos:
        q = deque()
        q.append(baechoos[0])
        while q:
            y, x = q.popleft()
            baechoos.remove([y, x])
            for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ny, nx = y + dy, x + dx
                if [ny, nx] in baechoos and [ny, nx] not in q:
                    q.append([ny, nx])
        answer += 1
    print(answer)