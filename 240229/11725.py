from collections import deque
n = int(input())
tree = [0] * (n+1)
tree[1] = 1
adj_arr = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int, input().split())
    adj_arr[a].append(b)
    adj_arr[b].append(a)
q = deque()
for i in adj_arr[1]:
    tree[i] = 1
    q.append(i)

while q:
    num = q.popleft()
    for i in adj_arr[num]:
        if tree[i] == 0:
            tree[i] = num
            q.append(i)
for i in range(2, n+1):
    print(tree[i])