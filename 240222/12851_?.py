import sys
sys.stdin = open('12851.txt')

from collections import deque
n, k = map(int, input().split())

queue = deque()
queue.append(n)
way = [0]*100001 # 최대 크기
cnt, result = 0,0
while queue:
    a =  queue.popleft()
    temp = way[a]
    if a == k: # 둘이 만났을 때
        result = temp # 결과
        cnt += 1 # 방문 횟수 +1
        continue
    
    for i in [a-1, a+1, a*2]:
        if 0 <= i < 100001 and (way[i] == 0 or way[i]== way[a] +1): #범위 안에있고 방문하지 않았거나, 다음 방문이 이전 방문+1이면
            way[i] = way[a] + 1
            queue.append(i) 

print(result)
print(cnt)