# 런타임 에러...

import sys
input = sys.stdin.readline
import copy

N, M, K = map(int, input().split())
# 초기 위치 저장
maze = [list(map(int, input().split())) for _ in range(N)]
people = [list(map(int, input().split())) for _ in range(M)]
exit = list(map(int, input().split()))
cnt = 0

# 위의 모두를 반영한 matrix 생성
maze_with_people = copy.deepcopy(maze)
for r, c in people:
    maze_with_people[r-1][c-1] = -1
    # 사람은 -1로 저장
maze_with_people[exit[0]-1][exit[1]-1] = -9
# 출구는 -9로 저장

def move(people):
    global cnt, exit, maze_with_people
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    # 상, 하, 좌, 우
    for p in range(len(people)):
        for d in range(4):
            if 0 <= people[p][0] -1 + dy[d] <N and 0<=people[p][1]-1 + dx[d]<N:
                if maze_with_people[people[p][0] -1 + dy[d]][people[p][1]-1 + dx[d]] == 0 and \
                    abs(people[p][0] + dy[d] - exit[0]) + abs(people[p][1] + dx[d] - exit[1]) < \
                    abs(people[p][0] - exit[0]) + abs(people[p][1] - exit[1]):
                    # 각 방향을 탐색했을 때 출구와의 최단거리가 가까워지는 방향이 있다면
                        maze_with_people[people[p][0]-1][people[p][1]-1] = 0
                        maze_with_people[people[p][0]-1 + dy[d]][people[p][1]-1 + dx[d]] = -1
                        people[p] =[people[p][0] + dy[d], people[p][1] + dx[d]]
                        # people의 위치를 업데이트하고
                        cnt+= 1
                        # 카운트
                        break
                    # 상하를 먼저 검색하고 존재하면 break로 종료
                    # 다음 사람으로 넘어감
                elif maze_with_people[people[p][0] -1 + dy[d]][people[p][1]-1 + dx[d]] == -9:
                    # 바로 출구가 있다면 출구로 가는 것이 최단거리
                    maze_with_people[people[p][0]-1][people[p][1]-1] = 0
                    people[p] = [0,0]
                    # 출구에 도착한 사람은 0,0으로 표시
                    cnt += 1

def search_square():
    min_l = N
    # 회전할 정사각형 찾는 함수
    for p in range(len(people)):
        min_l = min(min_l,max(abs(people[p][0]-exit[0]), abs(people[p][1]-exit[1])))
        # 가장 작은 정사각형의 길이 탐색 후

    check_mat = [[0]*N for _ in range(N)]
    for p in range(len(people)):
        if people[p] != [0,0]:
            check_mat[people[p][0]-1][people[p][1]-1] = 1
    check_mat[exit[0]-1][exit[1]-1] = 9
    # 체크용 행렬 구비

    sr, sc = N, N
    for i in range(N-min_l):
        for j in range(N-min_l):
            # 꼭지점 산출
            s = 0
            for r in range(i, i+min_l+1):
                for c in range(j, j+min_l+1):
                    s += check_mat[r][c]
            if s >= 10:
                sr = min(sr, i)
                if sr == i:
                    sc = min(sc, j)
                break
            else:
                continue
    # min_r, min_c와 exit가 그리는 가장 작은 정사각형의 왼쪽 위 꼭지점 구하기
    return [sr, sc, min_l]

def rotate(row, column, length):
    global people, exit, maze_with_people
    # 정한 정사각형을 회전시켜 반영하는 함수
    r_matrix = [[0]*(length+1) for _ in range(length+1)]

    for i in range(length + 1):
        for j in range(length + 1):
            if maze_with_people[row + i][column + j] > 0:
                r_matrix[j][length - i] = maze_with_people[row + i][column + j]-1
            else:
                r_matrix[j][length - i] = maze_with_people[row + i][column + j]
            # 시계방향으로 회전하여 다시 저장

    for i in range(length + 1):
        for j in range(length + 1):
            maze_with_people[row + i][column + j] = r_matrix[i][j]
            # 저장한 매트릭스를 반영

    people = []
    exit = []
    for r in range(N):
        for c in range(N):
            if maze_with_people[r][c] == -1:
                people.append([r+1, c+1])
            elif maze_with_people[r][c] == -9:
                exit = [r+1, c+1]
    # 새로운 people과 exit 위치 저장

def game(K):
    # K초 동안의 게임
    for _ in range(K):
        move(people)
        s = 0
        for p in people:
            s += sum(p)
        # people이 [0,0]으로만 이루어져 있지 않다면
        if s !=0:
            rotate(*search_square())
        # [0,0]로만 이루어져 모두 탈출했다면
        else:
            return

game(K)
print(cnt)
print(*exit)

