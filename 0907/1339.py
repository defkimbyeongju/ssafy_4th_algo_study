N = int(input())
# words = []
# alphabet = set()
# for _ in range(N):
#     word = input()
#     for w in word:
#         alphabet.add(w)
#     words.append(word)
# alphabet = list(alphabet)
# numbers = [i for i in range(9, -1, -1)][:len(alphabet)]
# max_hap = 0
#
#
# def hap(s, n, ns):
#     global max_hap
#     if s == n:
#         h = 0
#         alnum = dict()
#         for k in range(n):
#             alnum.setdefault(alphabet[k], ns[k])
#         for word in words:
#             for x in range(len(word)):
#                 h += alnum[word[x]] * (10 ** (len(word) - (x+1)))
#         max_hap = max(max_hap, h)
#     else:
#         for j in range(s, n):
#             ns[s], ns[j] = ns[j], ns[s]
#             hap(s+1, n, ns)
#             ns[s], ns[j] = ns[j], ns[s]
#
#
# hap(0, len(alphabet), numbers)
# print(max_hap)

words = []
alpha = []
alnum = dict()
for _ in range(N):
    word = input()
    for i in range(len(word)):
        if word[i] not in alpha:
            alpha.append(word[i])
            alnum.setdefault(word[i], 10 ** (len(word) - (i+1)))
        else:
            alnum[word[i]] += 10 ** (len(word) - (i+1))
numbers = [i for i in range(9, -1, -1)]
for a in range(len(alpha)):
    alpha[a] = [alpha[a], alnum[alpha[a]]]
alpha.sort(key=lambda x: x[1], reverse=True)
hap = 0
for n in range(len(alpha)):
    hap += alpha[n][1] * numbers[n]
print(hap)
