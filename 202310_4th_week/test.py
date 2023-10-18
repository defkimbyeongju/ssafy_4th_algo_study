N = 3
path = [-1] * N
nums = list(range(3))
def permutations(cnt):
    if cnt == N:
        print(path)
        return

    for i in nums:
        path[cnt] = i
        permutations(cnt + 1)
        path[cnt] = -1

permutations(0)