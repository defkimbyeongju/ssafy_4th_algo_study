N, M = map(int, input().split())
snowman_map = [list(map(int, input().split())) for _ in range(N)]
ground_info_list = list()

for y in range(N):
    if snowman_map[y][0] != 0:
        start = 0
        if snowman_map[y][0] == 2:
            snowman = len(ground_info_list)
        elif snowman_map[y][0] == 3:
            jewelry = len(ground_info_list)
    for x in range(1, M):
        formal_ground = snowman_map[y][x - 1]
        if snowman_map[y][x] == 0:
            if formal_ground != 0:
                end = x - 1
                ground_info_list.append((y, start, end))
        else:
            if formal_ground == 0:
                start = x

            if snowman_map[y][x] == 2:
                snowman = len(ground_info_list)
            elif snowman_map[y][x] == 3:
                jewelry = len(ground_info_list)

    if snowman_map[y][M - 1] != 0:
        ground_info_list.append((y, start, M - 1))

ground = len(ground_info_list)
adj_matrix = [[0] * ground for _ in range(ground)]
for adj_y in range(ground):
    now_y, now_start, now_end = ground_info_list[adj_y]
    for idx, (next_y, next_start, next_end) in enumerate(ground_info_list):
        for next_x in range(next_start, next_end + 1):
            if now_start <= next_x <= now_end:
                adj_matrix[adj_y][idx] = 1
                break

visited = [0] * ground
visited[jewelry] = 1
min_limit = 50


def dfs(now, final, limit):
    global is_arrived, min_limit
    if now == final:
        is_arrived = True
        return
    for next_ground, (ng_y, ng_sx, ng_ex) in enumerate(ground_info_list):
        if ground_info_list[now][0] - limit <= ng_y <= ground_info_list[now][0] + limit and next_ground != now:
            if not visited[next_ground] and adj_matrix[now][next_ground]:
                visited[next_ground] = 1
                dfs(next_ground, final, limit)
                visited[next_ground] = 0


is_arrived = False
limit = 0
while not is_arrived:
    limit += 1
    dfs(jewelry, snowman, limit)

print(limit)