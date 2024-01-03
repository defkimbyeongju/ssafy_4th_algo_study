first = input()
second = input()
len_f = len(first)
len_s = len(second)
max_len = 0
max_lcs = ''
for i in range(len_f):
    lcs = ''
    now = 0
    while i < len_f:
        for j in range(now, len_s):
            if second[j] == first[i]:
                i += 1
                lcs += second[j]
                now = j + 1
                break
        else:
            i += 1
    if len(lcs) > len(max_lcs):
        max_lcs = lcs
        max_len = len(lcs)
print(max_len)
if max_len:
    print(max_lcs)
