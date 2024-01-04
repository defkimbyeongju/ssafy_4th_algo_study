from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
cnt = [0]*(N+1)
children = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    children[A].append(B)
    # 자식들을 정리
    cnt[B] += 1
    # 각각 자기 앞에 있어야 하는 애들 수
dq = deque()
for a in range(1, N+1):
    if cnt[a] == 0:
        dq.append(a)
        # 자기 앞에 있어야 하는 것이 없는 애들을 디큐에 넣고
        cnt[a] -= 1
        # cnt에 표시
while dq:
    a = dq.pop()
    print(a, end=" ")
    # 자기 앞에 있어야 하는 애들이 없는 애들을 내보내고
    for b in children[a]:
        cnt[b] -= 1
        # 그들의 자식들에 대해 자기 앞에 있어야 하는 애들 수를 1씩 줄임

    for a in range(1, N+1):
        if cnt[a] == 0:
            dq.append(a)
            # 다시 자기 앞에 있어야 하는 애들이 없는 애들을 디큐에 넣고
            cnt[a] -= 1
            # cnt에 표시