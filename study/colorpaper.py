N = int(input())
arr = [[0]*100 for _ in range(100)]
for _ in range(N):
    a, b = map(int, input().split())
    for i in range(b, b+10):
        for j in range(a, a+10):
            arr[i][j] = 1
result = [a for item in arr for a in item]

print(sum(result))
