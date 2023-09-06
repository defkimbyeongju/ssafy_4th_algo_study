def change(i, S):
    if S[i] == '0':
        S[i] = '1'
    else:
        S[i] = '0'


N = int(input())
S1 = list(input())
S2 = S1[:]
E = list(input())
change(0, S2)
change(1, S2)
cnt1 = 0
cnt2 = 1
for n in range(1, N):
    if S1[n-1] != E[n-1]:
        for j in [n-1, n, n+1]:
            if 0 <= j < N:
                change(j, S1)
        cnt1 += 1
    if S2[n-1] != E[n-1]:
        for j in [n-1, n, n+1]:
            if 0 <= j < N:
                change(j, S2)
        cnt2 += 1
if S1 == E:
    print(cnt1)
elif S2 == E:
    print(cnt2)
else:
    print(-1)
