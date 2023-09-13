N, Q = map(int, input().split())
log_coordinates = [list(map(int, input().split())) for _ in range(N)]
can_jump_list = [[0] * N for _ in range(N)]
question_list = [list(map(int, input().split())) for _ in range(Q)]
for j in range(N):
    for i in range(j, N):
        if j == i:
            continue
        can_jump_log = 0
        min_jump = 1000000000
        for next_idx in range(N):
            if next_idx == j:
                continue
            now_x1, now_x2, now_y = log_coordinates[j]
            next_x1, next_x2, next_y = log_coordinates[next_idx]
            if next_x1 <= now_x2 <= next_x2 and abs(now_y - next_y) < min_jump:
                can_jump_log = next_idx

        if can_jump_log:
            can_jump_list[j][can_jump_log] = 1
            can_jump_list[can_jump_log][j] = 1

for start, end in question_list:
    can_jump = False
    queue = [start - 1]
    jumped = [0] * N
    jumped[start - 1] = 1
    while queue:
        now_idx = queue.pop(0)
        if now_idx == end - 1:
            can_jump = True
            break
        for next_idx in range(N):
            if can_jump_list[now_idx][next_idx] == 1 and not jumped[next_idx]:
                queue.append(next_idx)
                jumped[next_idx] = 1

    if can_jump:
        print(1)
    else:
        print(0)