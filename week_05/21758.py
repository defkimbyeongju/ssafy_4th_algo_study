N = int(input())
honey_list = list(map(int, input().split()))

# case_1
case_1 = sum(honey_list[1:N - 1]) + max(honey_list[1:N - 1])

# case_2
case_2_cannot = 10000 * N
index = 1

while index < N:
    if sum(honey_list[1:index]) > case_2_cannot:
        break
    else:
        case_2_cannot = min(case_2_cannot, honey_list[index] * 2 + sum(honey_list[1:index]))
    index += 1
case_2 = sum(honey_list[1:] * 2) - case_2_cannot

# case_3
honey_list_reverse = honey_list[::-1]
case_3_cannot = 10000 * N
index = 1

while index < N:
    if sum(honey_list_reverse[1:index]) > case_3_cannot:
        break
    else:
        case_3_cannot = min(case_3_cannot, honey_list_reverse[index] * 2 + sum(honey_list_reverse[1:index]))
    index += 1

case_3 = sum(honey_list_reverse[1:] * 2) - case_3_cannot

max_honey = max(case_1, case_2, case_3)
print(max_honey)
