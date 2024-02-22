import sys

sys.setrecursionlimit(100000)

input = sys.stdin.readline


def post_order(start, end):
    if start > end:
        return

    div = end + 1
    for i in range(start + 1, end + 1):
        if data[start] < data[i]:
            div = i
            break

    post_order(start + 1, div - 1)
    post_order(div, end)
    print(data[start])


data = []
while True:
    try:
        data.append(int(input().strip()))
    except:
        break

post_order(0, len(data) - 1)
