import sys
sys.stdin = open('22251.txt')
input = sys.stdin.readline

N, K, P, X = map(int, input().split())

# 1층 이상 N층 이하가 되도록 해야함
# K개의 표시등
# 최소 1개, 최대 P개를 반전시켜야함(획)
# 실제 X층에 멈춰있음

# 1층 이상 N층 이하가 되도록 해야함
# 최소 1개, 최대 P개를 반전시켜야함(획)



digitalnum = {
    0 : [1,1,1,1,1,1,0],
    1 : [0,0,0,0,1,1,0],
    2 : [1,0,1,1,0,1,1],
    3 : [1,0,0,1,1,1,1],
    4 : [0,1,0,0,1,1,1],
    5 : [1,1,0,1,1,0,1],
    6 : [1,1,1,1,1,0,1],
    7 : [1,0,0,0,1,1,0],
    8 : [1,1,1,1,1,1,1],
    9 : [1,1,0,1,1,1,1]
}

# 될 수 있는 최대 수
maxN = 0
for i in range(0, K):
    maxN += 9 * (10 ** i)


# 지금 K자리(6자리)인데 지금 14층(2자리)라면? 앞에 빈 자리만큼 0으로 채워줘야됨
x_str = str(X).zfill(K) # "000014"
nowfloor = [int(digit) for digit in x_str] # [0,0,0,0,1,4]


everynum = dict()

for i in range(10): 
    eachNum = dict()
    nowdigital = digitalnum[i]
    for key, value in digitalnum.items():
        # nownum 이랑 value랑 다른거 개수 = 반전시키는거 개수
        count = sum(x != y for x, y in zip(nowdigital, value))
        eachNum[key] = count
    everynum[i] = eachNum

cnt = 0

# 1층부터 999990층까지
for f in range(1, N + 1):
    if f == X:
        continue
    current = str(f).zfill(K)
    current = [int(digit) for digit in current] # 만약에 1층이랑 비교하면 [0,0,0,0,0,1]
    diff = 0
    for i in range(K): #nowfloor = [0,0,0,0,1,4]
        diff += everynum[nowfloor[i]][current[i]]
        if diff > P:
            break
    
    if diff <= P:
        cnt += 1
        # print(current)

print(cnt)

    
        # 지금 내 층이랑 nowfloor랑 비교해서 횟수가 많으면 카운트 안하고 
        





# print(everynum) # {0: {0: 3, 1: 5, 2: 4, 3: 2, 4: 3, 5: 0, 6: 1, 7: 4, 8: 2, 9: 1}}
# resarr = set()
# for key, value in everynum[0].items():
#     print(key, value)

        # [0,0,0,0,1,4]층
# def dfs(nownum, reversed, depth):
#     # 1층 이상 N층 이하가 되도록 해야함
#     # 최소 1개, 최대 P개를 반전시켜야함(획)
#     # K자리가 넘어가면 안됨
#     if depth >= K :
#         return
    
#     for key, reversed1 in everynum[depth].items(): # 
#         # print(key, reversed1, nownum)
#         newnum = nownum[:]
#         newnum[depth] = key
#         newreversed = reversed + reversed1
#         newnumber = int(''.join(map(str, newnum)))
#         if newnumber != X and (0< newnumber <= N) and newreversed <= P: # 현재 층이랑 다르면 안됨
#             resarr.add(newnumber)
#             dfs(newnum, newreversed, depth + 1)
#         dfs(nownum, reversed, depth+1)


# dfs(nowfloor, 0, 0) # [0,0,0,0,1,4]

# print(resarr)
# print(len(resarr))

