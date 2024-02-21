# 백준 2468 안전 영역

def deep(arr, height):  # 내린 비보다 숫자가 낮은 지역은 0으로 바꾸는 함수
    for i in range(N):
        for j in range(N):
            if arr[i][j] <= height:
                arr[i][j] = 0
def dfs(arr,i,j): # dfs로 문제 해결
    dir = [(0,1),(1,0),(-1,0),(0,-1)]
    for y, x in dir:
        ni, nj = i+y, j+x
        if 0<=ni<N and 0<=nj<N:
            if arr[ni][nj] != 0 and visited[ni][nj] == 0: # 침수되지 않았고, 방문하지 않은 지역은 방문 표시 해주기
                visited[ni][nj] = 1
                dfs(arr,ni,nj) # 재귀로 해당 좌표부터 시작해서 안전 영역 쭉 탐색해가기
import sys
sys.setrecursionlimit(10**7)
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
min_height = 21e8
max_height = 0
max_cnt = 1

for i in range(N):
    for j in range(N):
        if arr[i][j] < min_height:
            min_height = arr[i][j]
        if arr[i][j] > max_height:
            max_height = arr[i][j]

for i in range(min_height, max_height+1):  # 높이의 최소 ~ 최대치 범위만 반복하며 강수량이 얼마일 때 안전 영역이 제일 많은지 확인
    arr1 = arr
    cnt = 0
    deep(arr1, i)
    visited = [[0] * (N + 1) for _ in range(N + 1)]
    for j in range(N):
        for k in range(N):
            if arr1[j][k]!=0 and visited[j][k] == 0:
                visited[j][k] = 1
                dfs(arr1,j,k)
                cnt += 1 # dfs가 끝나면 인근 지역은 모두 탐색한 것이기 때문에 cnt 1 증가
    if max_cnt < cnt:
        max_cnt = cnt

print(max_cnt)