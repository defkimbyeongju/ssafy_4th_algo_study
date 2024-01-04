# from collections import deque

# def is_valid(x, y):
#     return 0 <= x < 3 and 0 <= y < 3

# def is_equal(board1, board2):
#     for i in range(3):
#         for j in range(3):
#             if board1[i][j] != board2[i][j]:
#                 return False
#     return True

# def BFS(board):
#     target = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
#     count = 0
#     queue = deque([(board, count)])
#     visited = set()

#     while queue:
#         current, count = queue.popleft()

#         if is_equal(current, target):
#             return count

#         # 이전에 방문한 상태를 문자열로 변환하여 집합에 추가
#         visited.add(''.join(map(str, current)))

#         for i in range(3):
#             for j in range(3):
#                 if current[i][j] == 0:
#                     x, y = i, j

#         for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
#             nx, ny = x + dx, y + dy

#             if is_valid(nx, ny):
#                 next_board = [row[:] for row in current]
#                 next_board[x][y], next_board[nx][ny] = next_board[nx][ny], next_board[x][y]

#                 # 이전에 방문한 상태가 아니라면 큐에 추가
#                 if ''.join(map(str, next_board)) not in visited:
#                     queue.append((next_board, count + 1))

#     return -1

# board = [list(map(int, input().split())) for _ in range(3)]
# result = BFS(board)
# print(result)

from collections import deque
import sys
input = sys.stdin.readline

def get_str(board):
    return ''.join(str(num) if num != 0 else '9' for row in board for num in row)

def bfs(start):
    target = '123456789'
    queue = deque([(start, 0)])
    visited = {start}

    while queue:
        current, count = queue.popleft()

        if current == target:
            return count

        zero_pos = current.index('9')
        x, y = divmod(zero_pos, 3)

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                nidx = nx * 3 + ny
                swap_board = list(current)
                swap_board[zero_pos], swap_board[nidx] = swap_board[nidx], swap_board[zero_pos]
                swap_str = ''.join(swap_board)

                if swap_str not in visited:
                    visited.add(swap_str)
                    queue.append((swap_str, count + 1))

    return -1

board = [list(map(int, input().split())) for _ in range(3)]
start = get_str(board)

result = bfs(start)
print(result)
