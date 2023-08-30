T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_p = 0
    for i in range(N-2):
        for j in range(i+2, N):
            for p in range(i+1, N-2):
                for q in range(p+2, N):
                    if i == p or i == q or j == p or j == q:
                        continue
                    elif p in range(i+1, j) and q in range(j+1, N):
                        continue
                    elif q in range(i+1, j) and p in range(j+1, N):
                        continue
                    elif abs(i-p) == 1 or abs(i-p) == N - 1 or abs(i-q) == 1 or abs(i-q) == N - 1:
                        continue
                    elif abs(j-p) == 1 or abs(j-p) == N - 1 or abs(j-q) == 1 or abs(j-q) == N - 1:
                        continue
                    elif j - i == N - 1 or q - p == N - 1:
                        continue
                    pas = (arr[i] + arr[j]) ** 2 + (arr[p] + arr[q]) ** 2
                    if max_p < pas:
                        max_p = pas
    print(f'#{tc}', max_p)
