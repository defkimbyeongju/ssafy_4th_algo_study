N = int(input())
inouts = input()
# in = 0, out = 1, no = 2
counts = [0, 0, 0]
answer = 'Yes'

def check():
    if counts[0] + counts[2] >= counts[1]:
        return True
    else:
        return False

if N % 2:
    answer = 'No'
else:
    for inout in inouts:
        if inout == '(':
            counts[0] += 1
        elif inout == ')':
            counts[1] += 1
        else:
            counts[2] += 1
        if not check():
            answer = 'No'
            break

if counts[0] > counts[1] + counts[2]:
    answer = 'No'

print(answer)