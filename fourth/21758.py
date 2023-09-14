import sys

input = sys.stdin.readline

N = int(input())
honey = list(map(int, input().split()))
honey_sum = [honey[0]]
for i in range(1,N):
    honey_sum.append(honey_sum[i-1]+honey[i])

result = 0
for i in range(1,N-1):
    result = max(result, (honey_sum[N-1]*2)-honey[0]-honey_sum[i]-honey[i])

for i in range(1,N-1):
    result = max(result, honey_sum[N-2]-honey[i]+honey_sum[i-1])
for i in range(1,N-1):
    result = max(result, honey_sum[N-2]-honey[0]+honey[i])

print(result)
