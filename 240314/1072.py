import math

X, Y = map(int, input().split())
now = int((Y * 100) / X)
if now >= 99:
    print(-1)
    quit()
i = ((now + 1) * X - 100 * Y) / (99 - now)
print(math.ceil(i))
print(1 / 3 * 100)