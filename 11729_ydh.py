n = int(input())
result_lst = []


def hanoi_tower(n, start, tmp, goal):
    if n == 1:
        result_lst.append((start, goal))
        return
    hanoi_tower(n - 1, start, goal, tmp)
    result_lst.append((start, goal))
    hanoi_tower(n - 1, tmp, start, goal)



hanoi_tower(n, 1, 2, 3)
print(len(result_lst))
for i in result_lst:
    print(*i)

