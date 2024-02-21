# 활용 알고리즘: 완전탐색(조합) -> 깨뜨릴 벽돌 정하기 위해 & BFS -> 벽돌 깼을 때 영향을 받는 다른 벽돌들 처리하기 위해
# 함수를 두 개로 나눈다.
# 1. 재귀로 모든 조합을 실행하며 벽돌을 깨는 함수
# 2. 벽돌을 아래로 미는 함수

from collections import deque
import copy
dir = [(0,1),(1,0),(0,-1),(-1,0)]
def breaking(n, lst): # 벽돌 깨기. n은 현재 돌린 조합, lst는 현재 상태의 벽돌 정보
    global min_v
    if n == N:
        temp = 0
        for i in range(H): # 행으로 순회
            temp += lst[i].count(0)
        res = W*H - temp # 전체에서 깨진 벽돌의 개수를 빼주면 결과임
        min_v = min(min_v, res) # 최소값 갱신
        return
    temporary = sum(lst, [])
    if sum(temporary) == 0:  # 남은 숫자가 없으면 종료. 가지치기
        min_v = 0
        return
    for i in range(W): # 열 우선 순회
        new_lst = copy.deepcopy(lst) # 열이 바뀔 때마다 copy를 해줘야 재귀를 돌고 와도 영향을 안받음
        for j in range(H):
            if new_lst[j][i] != 0: # 0이 아니라면
                q = deque()
                q.append([j,i,new_lst[j][i]]) # 행, 열, power 순서
                new_lst[j][i] = 0
                while q:
                    nj, ni, power = q.popleft()
                    if power == 1:
                        continue
                    for x,y in dir:
                        for him in range(1,power):
                            ny, nx = nj+x*him, ni+y*him # 다음 행, 다음 열
                            if 0>nx or 0>ny or nx>=W or ny>=H:
                                break
                            if new_lst[ny][nx] != 0:
                                q.append([ny,nx,new_lst[ny][nx]])
                                new_lst[ny][nx] = 0 # 같은 좌표가 중복으로 담기는 걸 방지하기 위해
                new_lst = push(new_lst) # 살아남은 벽돌들은 아래로 쭉 밀어줌
                breaking(n+1, new_lst)
                break # 다시 재귀에서 돌아왔을 때, 이 밑으로 보는 건 의미가 없다. 각 열의 제일 위에 있는 벽돌만 깨야 하기 때문에


def push(lst): # 벽돌 아래로 밀기
    for i in range(W):
        for j in range(H-1, 0, -1): # 열의 제일 아래서부터 확인
            if lst[j][i] == 0: # 아래서부터 비어 있는 칸이 있으면 
                for k in range(j-1, -1, -1): # 위칸부터 남아 있는 벽돌 끌어 내리기
                    if lst[k][i] != 0:
                        lst[j][i], lst[k][i] = lst[k][i], lst[j][i]
                        break # 자리 바꿨으면 break
    return lst
    

T = int(input())
for tc in range(1,T+1):
    N, W, H = map(int, input().split()) # N은 떨어뜨릴 벽돌 개수, W은 폭(즉, x축), H는 높이(즉, y축)
    arr = [list(map(int, input().split())) for _ in range(H)]
    min_v = 21e8
    breaking(0, arr)
    print(f'#{tc} {min_v}')