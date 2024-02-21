'''
N = int(input())

lines = list(map(int, input().split()))

d = [0] * (N+1)

for i in range(1,N+1):
    max_v = -1
    idx = -1
    for j in range(i-1):
        if lines[j] < lines[i-1] and lines[j] > max_v:
            max_v = lines[j]
            idx = j
    if max_v == -1:
        d[i] = 1
    else:
        d[i] = d[idx+1] + 1
print(N-max(d))
'''

N = int(input())

lines = list(map(int, input().split()))

d = [0] * (N+1)

for i in range(1, N+1):
