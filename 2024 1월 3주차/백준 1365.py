def binary_search(sub, val):
    left, right = 0, len(sub) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if sub[mid] < val:
            left = mid + 1
        else:
            right = mid - 1
    return left

def min_cut(connections):
    sub = []
    for val in connections:
        pos = binary_search(sub, val)
        if pos == len(sub):
            sub.append(val)
        else:
            sub[pos] = val
    return len(connections) - len(sub)

N = int(input())
connections = list(map(int, input().split()))
print(min_cut(connections))