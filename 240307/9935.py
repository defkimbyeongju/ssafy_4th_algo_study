# 자료구조 어떻게 해결해야 할까?
# 파이썬 문자열 find 메서드는 O(N)의 시간 복잡도를 갖는다.
# 정답 코드는 시간복잡도 O(n * m)
# 오답 코드는 O(n^2)

## 오답 코드
# word = input()
# bomb = input()
#
# while True:
#     d= 1
#     for i in range(len(word) - len(bomb)+1):
#         if word[i:i+len(bomb)] == bomb:
#             word = word.replace(bomb, '')
#             break
#     else:
#         break
# if not word:
#     print('FRULA')
# else:
#     print(word)


word = input()
bomb = list(input())
n = len(bomb)
stack = []
for w in word:
    stack.append(w)
    if stack[-n:] == bomb:
        for _ in range(n):
            stack.pop(-1)
print(''.join(stack) if stack else 'FRULA')
