# 세그먼트 트리
# 1. 트리 초기화
# 	- 리프 노드의 개수가 데이터 개수 이상이 되도록 트리 리스트 만들기
# 	- 2^k >= N(데이터의 수)을 만족하는 k의 최솟값을 구한 후 2^k * 2 를 트리 배열의 크기로 설정
# 	- 리프노드의 트리배열 시작위치를 2^k 로 설정
# 2. 질의값 구하기
# 	질의 인덱스를 세그먼트 트리 인덱스로 변경하는 방법
# 	    - 세그먼트 트리 index = 주어진 질의 index + 2^k -1
# 	질의값 구하는 과정
# 		- start_index % 2 == 1 일 때 해당 노드 keep
# 		- end_index % 2 == 0 일 떄 해당 노드 keep
# 		- start_index depth 변경 : end_index = (end_index + 1) // 2
# 		- end_index depth 변경 : end_index = (end_index - 1) // 2
# 		- end_index < start_index가 되면 종료

# sol1
def init(node, start, end):
    # 세그먼트 트리 생성
    # node: 현재 노드, start와 end: 구간의 시작과 끝 인덱스
    if start == end:
        # 리프 노드에 도달했을 때, 배열의 값을 세그먼트 트리에 저장
        tree[node] = nums[start]
    else:
        # 리프 노드가 아니면 구간을 반으로 나누어 재귀
        mid = (start + end) // 2
        tree[node] = init(node*2, start, mid) + init(node*2+1, mid+1, end)
    return tree[node]

def update(node, start, end, index, diff):
    # 세그먼트 트리의 특정 인덱스 값을 업데이트
    if index < start or index > end:
        # 변경하려는 인덱스가 범위 밖에 있을 경우 함수를 종료
        return
    tree[node] += diff
    # 리프 노드가 아닐 경우 자식 노드도 업데이트
    if start != end:
        mid = (start + end) // 2
        update(node*2, start, mid, index, diff)
        update(node*2+1, mid+1, end, index, diff)

def query(node, start, end, left, right):
    # 구간 합을 계산
    if left > end or right < start:
        # 구간이 겹치지 않을 경우
        return 0
    if left <= start and end <= right:
        # 구간이 완전히 포함될 경우
        return tree[node]
    # 구간을 나누어 재귀
    mid = (start + end) // 2
    return query(node*2, start, mid, left, right) + query(node*2+1, mid+1, end, left, right)

N, M, K = map(int, input().split())
nums = [int(input()) for _ in range(N)]
tree = [0] * (4*N)
init(1, 0, N-1)

for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        # 값 변경
        diff = c - nums[b-1]
        nums[b-1] = c
        update(1, 0, N-1, b-1, diff)
    else:
        # 구간 합 계산
        print(query(1, 0, N-1, b-1, c-1))

# sol2
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

# 세그먼트 트리의 높이
tree_height = 0
length = n
while length != 0:
    length //= 2
    tree_height += 1

# 세그먼트 트리의 전체 크기
tree_size = pow(2, tree_height + 1) # pow(a, b) = a ^ b

# 리프 노드의 시작 인덱스
left_node_start_index = tree_size // 2 - 1

tree = [0] * (tree_size + 1)

for i in range(left_node_start_index + 1, left_node_start_index + n + 1):
    tree[i] = int(input())

# 세그먼트 트리 생성
def set_tree(i):
    while i != 1:
        tree[i // 2] += tree[i]
        i -= 1

# 세그먼트 트리 초기화
set_tree(tree_size - 1)

# 데이터 변경 함수
def change_val(index, value):
    diff = value - tree[index]
    while index > 0:
        tree[index] += diff
        index = index // 2

# 구간 합 계산 함수
def get_sum(s, e):
    part_sum = 0
    while s <= e:
        if s % 2 == 1:
            part_sum += tree[s]
            s += 1
        if e % 2 == 0:
            part_sum += tree[e]
            e -= 1
        s //= 2
        e //= 2
    return part_sum

for _ in range(m + k):
    question, s, e = map(int, input().split())
    if question == 1:
        change_val(left_node_start_index + s, e)
    elif question == 2:
        s += left_node_start_index
        e += left_node_start_index
        print(get_sum(s, e))
