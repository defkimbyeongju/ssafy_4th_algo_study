import sys
sys.stdin = open('test.txt')

# 최장 증가 수열
n = int(input())
arr = list(map(int, input().split()))
d = []

def bisect(e, value):
    s = 0
    while s < e:
        mid = (s + e) // 2
        if value < d[mid]:
            e = mid
        else:
            # s = mid 이렇게 하면 시간 초과 남
            s = mid + 1
    return e

for i in range(n):
    if i == 0:
        d.append(arr[i])
    elif arr[i] > d[-1]:
        d.append(arr[i])
    else:
        idx = bisect(len(d), arr[i])
        if arr[i] < d[idx]: # 이 줄 없어도 맞다고 나옴 근데 이유 모름..
            d[idx] = arr[i]


print(n-len(d))