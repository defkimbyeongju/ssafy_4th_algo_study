N = int(input())
buildings = list(map(int, input().split()))
answer = 0
for k in range(N):
    cnt = 0
    now = buildings[k]

    for l in range(k - 1, -1, -1):
        left = buildings[l]
        diff = now - left
        for lb in range(l + 1, k):
            if left + diff * (lb - l) / (k - l) <= buildings[lb]:
                break
        else:
            cnt += 1
    
    for r in range(k + 1, N):
        right = buildings[r]
        diff = now - right
        for rb in range(k + 1, r):
            if right + diff * (r - rb) / (r - k) <= buildings[rb]:
                break
        else:
            cnt += 1
    
    answer = max(answer, cnt)
print(answer)