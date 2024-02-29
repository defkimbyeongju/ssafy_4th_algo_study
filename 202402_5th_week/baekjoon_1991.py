# 트리 순회

# 노드 갯수
N = int(input())

# 이진트리 기록할 dict
tree_dict = {}
for i in range(65, 65 + N):
    tree_dict[chr(i)] = []

# 주어진 입력대로 이진트리 작성
for _ in range(N):
    root, left, right = input().split()
    tree_dict[root].append(left)
    tree_dict[root].append(right)

# 결과값 기록할 변수
pre_result = ""
in_result = ""
post_result = ""

# 전위 순회
def preorder(root):
    global pre_result

    left = tree_dict[root][0]
    right = tree_dict[root][1]

    # 루트 출력
    pre_result += root

    # 왼쪽탐색
    if left != '.':
        preorder(left)

    # 오른쪽탐색
    if right != '.':
        preorder(right)


# 중위 순회
def inorder(root):
    global in_result

    left = tree_dict[root][0]
    right = tree_dict[root][1]

    # 왼쪽탐색
    if left != '.':
        inorder(left)

    # 루트 출력
    in_result += root

    # 오른쪽탐색
    if right != '.':
        inorder(right)


# 후위 순회
def postorder(root):
    global post_result

    left = tree_dict[root][0]
    right = tree_dict[root][1]

    # 왼쪽탐색
    if left != '.':
        postorder(left)

    # 오른쪽탐색
    if right != '.':
        postorder(right)

    # 루트 출력
    post_result += root

# 함수 호출
preorder("A")
inorder("A")
postorder("A")


# 최종 결과 출력
print(pre_result)
print(in_result)
print(post_result)