string = list(input())
explode = list(input())
length = len(explode)
answer = []
for c in string:
    answer.append(c)
    if answer[len(answer) - length:] == explode:
        for _ in range(length):
            answer.pop()
print(*answer, sep='') if answer else print('FRULA')
