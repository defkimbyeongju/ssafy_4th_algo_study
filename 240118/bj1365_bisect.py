import sys
from bisect import bisect_left

n = int(sys.stdin.readline())
line = list(map(int, sys.stdin.readline().split()))
res = []

for i in range(n):
    if i == 0:  # 첫 번째 수는 res에 추가
        res.append(line[0])
    if res[-1] < line[i]:   # line[i]가 res의 마지막 요소보다 크면 마지막에 추가
        res.append(line[i])
    else:   # line[i]가 res의 마지막 요소보다 작으면 이분탐색 하여 나온 index위치의 값과 교환
        tmp = bisect_left(res, line[i])
        
        res[tmp] = line[i]


print(n - len(res))