N, S = map(int, input().split())
sequence = list(map(int, input().split()))
hap = 0
count = 0
answer = 9e9
for i, n in enumerate(sequence, 1):
    hap += n
    count += 1
    while hap >= S:
        answer = min(answer, count)
        hap -= sequence[i - count]
        count -= 1
print(answer) if answer != 9e9 else print(0)