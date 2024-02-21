'''
N = int(input())
buildings = list(map(int, input().split()))
max_v = 0
def look(i, arr):
    result = 0
    count = 1
    max_lean = 0
    min_lean = 0
    again_1 = False
    again_2 = False
    for building in arr:
        lean = (buildings[i]-building) / count
        if lean >= 0:
            if lean > max_lean:
                result += 1
                max_lean = lean
                again_1 = False
            elif lean == max_lean and not again_1:
                result += 1
                again_1 = True
        else:
            if lean < min_lean:
                result += 1
                min_lean = lean
                again_2 = False
            elif lean == min_lean and not again_2:
                result += 1
                again_2 = True
        count += 1
    return result

if N == 1:
    print(0)
else:
    for i in range(N):
        if i == 0:
            temp = look(i, buildings[i+1:])
        elif i == N-1:
            temp = look(i, buildings[i-1::-1])
        else:
            temp = look(i, buildings[i+1:]) + look(i,buildings[i-1::-1])
        max_v = max(temp, max_v)
    print(max_v)
'''

N = int(input())
buildings = list(map(int, input().split()))
result = [0]*N

for i in range(N-1) :
  max_slope = -float('inf')
  for j in range(i+1, N) :
    slope = (buildings[j] - buildings[i]) / (j - i)
    if slope <= max_slope :
      continue
    max_slope = max(max_slope, slope)
    result[i] += 1
    result[j] += 1
print(max(result))


