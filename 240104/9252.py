first = '0' + input()
second = '0' + input()
len_f = len(first)
len_s = len(second)
arr = [[0] * (len_s) for _ in range(len_f)]
for i in range(1, len_f):
    for j in range(1, len_s):
        if first[i] == second[j]:
            arr[i][j] = arr[i - 1][j - 1] + 1
        else:
            arr[i][j] = max(arr[i - 1][j], arr[i][j - 1])
lcs = ''
y, x = len_f - 1, len_s - 1
while y > 0 and x > 0:
    now = arr[y][x]
    if now == arr[y - 1][x]:
        y -= 1
    elif now == arr[y][x - 1]:
        x -= 1
    else:
        lcs = first[y] + lcs
        y -= 1
        x -= 1
print(len(lcs))
if lcs:
    print(lcs)


# max_len = 0
# max_lcs = ''
# for i in range(len_f):
#     lcs = ''
#     now = 0
#     while i < len_f:
#         for j in range(now, len_s):
#             if second[j] == first[i]:
#                 i += 1
#                 lcs += second[j]
#                 now = j + 1
#                 break
#         else:
#             i += 1
#     if len(lcs) > len(max_lcs):
#         max_lcs = lcs
#         max_len = len(lcs)
# print(max_len)
# if max_len:
#     print(max_lcs)
