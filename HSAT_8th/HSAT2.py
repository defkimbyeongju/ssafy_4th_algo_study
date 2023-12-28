import sys
from collections import deque

sys.stdin = open('HSAT2.txt')
input = sys.stdin.readline

n, m = map(int, input().split()) # 동전 개수, 거슬러줘야 하는 돈

coinA = []
coinB = []

for _ in range(n):
    t, v = input().split()
    if t == 'A': # A는 중복 가능
        coinA.append(int(v))
    else: # B는 중복 안됨
        coinB.append(int(v))

cntB = len(coinB)

memo = [0] * (m * 2 + 1) 


def bfs():
    q = deque([])

    for a in coinA:
        memo[a] = 1
        q.append((a, [False] * cntB))
    
    
    for b in range(cntB):
        default = [False] * cntB
        value = coinB[b]
        memo[value] = 1
        default[b] = True
        q.append((value, default))
    
    while q:
        now, useB = q.popleft()
        for a in coinA:
            if now + a > m * 2:
                return
            if memo[now + a] == 0 or (memo[now + a] > memo[now] + 1):
                memo[now + a] = memo[now] + 1
                q.append((now+a, useB))
        for b in range(cntB):
            if not useB[b]:
                copy = useB[:]
                copy[b] = True
                valueB = coinB[b]
                if now + valueB > m * 2:
                    break
                if memo[now + valueB] == 0 or (memo[now + valueB] > memo[valueB] + 1) :
                    memo[now + valueB] = memo[now] + 1
                    q.append((now+valueB, copy))
    return 0



bfs()

# print(memo[:12])
print(memo[m])




# 3 8
# A 1
# A 2
# B 4



