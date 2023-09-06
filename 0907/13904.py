N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(reverse=True)
stack = []
ans = 0
for day in range(arr[0][0], 0, -1):
    for task in arr:
        if task[0] > day:
            continue
        elif task[0] == day:
            stack.append(task[1])
        else:
            break
    if stack:
        ans += max(stack)
        stack.pop(stack.index(max(stack)))
print(ans)
