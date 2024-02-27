# 트리의 부모 찾기

# BFS
def BFS():
    



# 노드 갯수
N = int(input())

# 인접리스트
line_list = [[] for i in range(N + 1)]

# 인접리스트 정보 입력
for i in range(N - 1):
    a, b = int(input().split())
    line_list[a].append(b)
    line_list[b].append(a)

