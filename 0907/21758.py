N = int(input())
arr = list(map(int, input().split()))
total = sum(arr)
hap1 = (total - arr[0] - arr[1]) * 2
hap2 = (total - arr[N-1] - arr[N-2]) * 2
max_hap = max(total + max(arr[1:N-1]) - arr[0] - arr[N-1], hap1, hap2)
for i in range(2, N-1):
    hap1 = hap1 + arr[i - 1] - (arr[i] * 2)
    hap2 = hap2 + arr[N - i] - (arr[N - (i + 1)] * 2)
    max_hap = max(max_hap, hap1, hap2)
print(max_hap)
