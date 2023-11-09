# 코드트리 삼성 SW 역량테스트 기출문제 루돌프의 반란
N, M, P, C, D = map(int, input().split())
santas = [[0, 0, 0] for _ in range(P + 1)]
Rr, Rc = map(int, input().split())
santas[0] = [Rr, Rc, 0]  # -1: 탈락 / 0: 기본 / 0<: 기절
for _ in range(P):
    Pn, Sr, Sc = map(int, input().split())
    santas[Pn] = [Sr, Sc, 0]

scores = [0] * (P + 1)


# 상호작용
def santa_move(collided, r, c, dr, dc):
    santas[collided] = [r, c, santas[collided][2]]

    for other, [other_r, other_c, other_s] in enumerate(santas):
        if other_s == -1:
            continue

        if other == 0 or other == collided:
            continue

        if other_r == r and other_c == c:
            if 1 <= other_r + dr <= N and 1 <= other_c + dc <= N:
                santa_move(other, other_r + dr, other_c + dc, dr, dc)
            else:
                santas[other] = [-1, -1, -1]

            return


turn = 1
while turn <= M:
    # 게임 종료 여부
    is_end = True
    
    # 기절 턴 지나기
    for santa, [santa_r, santa_c, santa_s] in enumerate(santas):
        if santa == 0:
            continue

        if santa_s >= 0:
            is_end = False

        if santa_s > 0:
            santas[santa][2] -= 1
    
    # 게임 종료
    if is_end:
        break

    # 턴 진행
    dir_r, dir_c = 0, 0
    min_distance = (N - 1) ** 2 + (N - 1) ** 2 + 1
    min_r, min_c = 0, 0
    [rudolph_r, rudolph_c, rudolph_s] = santas[0]

    # 루돌프의 돌진 방향 탐색
    for santa, [next_r, next_c, next_s] in enumerate(santas):
        if santa == 0:
            continue

        if next_s < 0:
            continue

        distance = (next_r - rudolph_r) ** 2 + (next_c - rudolph_c) ** 2

        if distance > min_distance:
            continue

        if distance == min_distance:
            if next_r < min_r:
                continue

            if next_r == min_r:
                if next_c < min_c:
                    continue

        min_distance = distance
        min_r, min_c = next_r, next_c

        dir_r = 0 if next_r - rudolph_r == 0 else int((next_r - rudolph_r) / abs(next_r - rudolph_r))
        dir_c = 0 if next_c - rudolph_c == 0 else int((next_c - rudolph_c) / abs(next_c - rudolph_c))

    # 루돌프의 움직임
    rudolph_r = rudolph_r + dir_r
    rudolph_c = rudolph_c + dir_c

    santas[0] = [rudolph_r, rudolph_c, 0]

    # 루돌프 -> 산타 충돌
    for santa, [santa_r, santa_c, santa_s] in enumerate(santas):
        if santa == 0:
            continue

        if santa_s < 0:
            continue

        # 루돌프가 움직일 자리에 산타가 있다면
        if santa_r == rudolph_r and santa_c == rudolph_c:
            scores[santa] += C
            next_r = santas[santa][0] + dir_r * C
            next_c = santas[santa][1] + dir_c * C
            santas[santa][2] = 2

            # 게임판 안으로 밀려난 산타
            if 1 <= next_r <= N and 1 <= next_c <= N:
                santas[santa][0] = next_r
                santas[santa][1] = next_c
                santa_move(santa, next_r, next_c, dir_r, dir_c)
            # 게임판 밖으로 밀려난 산타
            else:
                santas[santa] = [-1, -1, -1]

            break

    # 산타의 움직임
    for santa, [santa_r, santa_c, santa_s] in enumerate(santas):
        min_distance = (N - 1) ** 2 + (N - 1) ** 2 + 1
        min_dr, min_dc = 0, 0

        if santa == 0:
            continue

        if santa_s != 0:
            continue

        # 네 방향 중 가능한 방향으로 이동
        for dir_r, dir_c in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            if 1 <= santa_r + dir_r <= N and 1 <= santa_c + dir_c <= N:
                now_distance = (santa_r - rudolph_r) ** 2 + (santa_c - rudolph_c) ** 2
                next_distance = (santa_r + dir_r - rudolph_r) ** 2 + (santa_c + dir_c - rudolph_c) ** 2

                if now_distance <= next_distance:
                    continue

                if next_distance >= min_distance:
                    continue

                no_santa = True
                for next_santa, [next_r, next_c, next_s] in enumerate(santas):
                    if next_santa == 0:
                        continue

                    if next_r == santa_r + dir_r and next_c == santa_c + dir_c:
                        no_santa = False
                        break

                if no_santa:
                    min_distance = next_distance
                    min_dr, min_dc = dir_r, dir_c

        # 이동 불가능
        if min_dr == 0 and min_dc == 0:
            continue

        next_r, next_c = santa_r + min_dr, santa_c + min_dc
        # 산타 -> 루돌프 충돌
        if next_r == rudolph_r and next_c == rudolph_c:
            scores[santa] += D
            next_r = next_r - min_dr * D
            next_c = next_c - min_dc * D
            santas[santa][2] = 2
            # 상호작용 확인
            if 1 <= next_r <= N and 1 <= next_c <= N:
                santa_move(santa, next_r, next_c, -min_dr, -min_dc)
            else:
                santas[santa] = [-1, -1, -1]
        else:
            santa_move(santa, next_r, next_c, min_dr, min_dc)

    # 탈락하지 않은 산타 점수 획득
    for santa in range(1, P + 1):
        if santas[santa][2] == -1:
            continue

        scores[santa] += 1

    turn += 1

print(*scores[1:])
