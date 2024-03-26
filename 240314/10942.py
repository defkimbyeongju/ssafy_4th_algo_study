N = int(input())
sequence = list(map(int, input().split()))
    
palindrome = [[n] for n in range(N)]
for k in range(1, N):
    s, e = 0, k
    while s < e:
        if sequence[s] == sequence[e]:
            s, e = s + 1, e - 1
        else:
            break
    else:
        s, e = 0, k
        while s < e:
            palindrome[s].append(e)
            s, e = s + 1, e - 1

    if k != N - 1:
        s, e = N - (k + 1), N - 1
        while s < e:
            if sequence[s] == sequence[e]:
                s, e = s + 1, e - 1
            else:
                break
        else:
            s, e = N - (k + 1), N - 1
            while s < e:
                palindrome[s].append(e)
                s, e = s + 1, e - 1

M = int(input())
for _ in range(M):
    S, E = map(int, input().split())
    S, E = S - 1, E - 1
    print(int(E in palindrome[S]))