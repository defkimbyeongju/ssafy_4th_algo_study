'''
def chicken_distance(used, houses): # 치킨 거리를 구하는 함수
    global min_chicken
    total = 0
    for hy, hx in houses:
        min_v = 1e9
        for i in range(len(used)):
            if used[i]:
                for cy, cx in chickens[i]:
                    temp = abs(hy-cy) + abs(hx-cx)
                    min_v = min(temp, min_v)
        total += min_v
        if total >= min_chicken: # 가지치기
            return
    min_chicken = total # 최소 치킨 거리 값 최신화

def remain_chicken(used, M, start):
    if sum(used) == M:
        chicken_distance(used, houses)
        return
    for i in range(start, len(chickens)):
        if not used[i]:
            used[i] = 1
            remain_chicken(used, M, start+1)
            used[i] = 0
'''

# 남겨둘 치킨집을 조합으로 정하기. 완전 탐색 기법 적용
def combinations(arr, k):
    def backtrack(start, current_combination):
        if len(current_combination) == k:
            result.append(current_combination[:])
            return
        for i in range(start, len(arr)):
            current_combination.append(arr[i])
            backtrack(i + 1, current_combination)
            current_combination.pop()

    result = []
    backtrack(0, [])
    return result

import sys
N,M = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
houses = []
chickens = []
min_chicken = 1e9
for i in range(N): # house와 chicken 리스트에 좌표 추가
    for j in range(N):
        if arr[i][j] == 1:
            houses.append((i,j))
        elif arr[i][j] == 2:
            chickens.append((i,j))
res = combinations(chickens, M) # 조합으로 구한 M개의 치킨 가게가 남아 있는 경우의 수를 res 리스트에 저장하고 결과 계산
result = 1e9
for i in range(len(res)): # 가능한 조합의 수만큼 반복
    total = 0
    for hy, hx in houses: # 각 집에서 가장 가까운 치킨집을 구함
        temp = 1e9
        for j in range(M):
            temp = min(temp, abs(res[i][j][0] - hy) + abs(res[i][j][1] - hx))
        total += temp # 각 집의 좌표별로 가장 가까운 치킨집과의 거리를 더해줌.
    result = min(result, total) # 최소값을 계속 갱신해주기
print(result)