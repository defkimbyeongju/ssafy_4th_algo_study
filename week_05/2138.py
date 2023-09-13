import copy

N = int(input())
before = list(map(int, input()))
after = list(map(int, input()))

first = copy.deepcopy(before)
first_case = 0
for index in range(1, N - 1):
    if first[index - 1] != after[index - 1]:
        first_case += 1
        first[index - 1] = int(not first[index - 1])
        first[index] = int(not first[index])
        first[index + 1] = int(not first[index + 1])
if first[N - 2] != after[N - 2]:
    first_case += 1
    first[N - 2], first[N - 1] = int(not first[N - 2]), int(not first[N - 1])
if first != after:
    first_case = -1

second = copy.deepcopy(before)
second_case = 1
second[0], second[1] = int(not second[0]), int(not second[1])
for index in range(1, N - 1):
    if second[index - 1] != after[index - 1]:
        second_case += 1
        second[index - 1] = int(not second[index - 1])
        second[index] = int(not second[index])
        second[index + 1] = int(not second[index + 1])
if second[N - 2] != after[N - 2]:
    second_case += 1
    second[N - 2], second[N - 1] = int(not second[N - 2]), int(not second[N - 1])
if second != after:
    second_case = -1

if first_case == -1:
    if second_case == -1:
        print(-1)
    else:
        print(second_case)
else:
    if second_case == -1:
        print(first_case)
    else:
        print(min(first_case, second_case))
