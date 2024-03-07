string = list(input())
explode = list(input())
length = len(explode)
answer = []
for c in string:
    answer.append(c)
    if answer[-1:-(length + 1):-1] == explode[::-1]:
        for _ in range(length):
            answer.pop()
print(*answer, sep='') if answer else print('FRULA')