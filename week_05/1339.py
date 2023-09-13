N = int(input())
word_list = [list(input()) for _ in range(N)]
letter_list = list()
for word in word_list:
    for letter in word:
        if letter not in letter_list:
            letter_list.append(letter)

frequency_list = [0] * len(letter_list)

for word in word_list:
    digit = 0
    for letter in word[::-1]:
        frequency_list[letter_list.index(letter)] = frequency_list[letter_list.index(letter)] + 10 ** digit
        digit += 1

frequency_list.sort(reverse=True)
start = 9
max_sum = 0
for frequency in frequency_list:
    max_sum += frequency * start
    start -= 1
print(max_sum)