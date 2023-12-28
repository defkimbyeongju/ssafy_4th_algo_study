from collections import deque

def to_2d_list(s):
    return [list(map(int, s[i:i+3])) for i in range(0, 9, 3)]

def to_string(board):
    return ''.join(map(str, [num for row in board for num in row]))

def is_target(board):
    return board == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

def swap(board, i1, j1, i2, j2):
    new_board = [row[:] for row in board]
    new_board[i1][j1], new_board[i2][j2] = new_board[i2][j2], new_board[i1][j1]
    return new_board

def get_neighbors(board, i, j):
    neighbors = []
    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if 0 <= i + di < 3 and 0 <= j + dj < 3:
            neighbors.append(swap(board, i, j, i + di, j + dj))
    return neighbors

def bfs(start_board):
    queue = deque([(start_board, 0)])
    visited = set([to_string(start_board)])
    while queue:
        current_board, moves = queue.popleft()

        if is_target(current_board):
            return moves

        i, j = next((i, j) for i in range(3) for j in range(3) if current_board[i][j] == 0)

        for neighbor in get_neighbors(current_board, i, j):
            neighbor_str = to_string(neighbor)
            if neighbor_str not in visited:
                visited.add(neighbor_str)
                queue.append((neighbor, moves + 1))
    return -1

# 입력 받기
input_string = ''.join(["".join(input().split()) for _ in range(3)])
start_board = to_2d_list(input_string)

# BFS 실행
result = bfs(start_board)
print(result)
