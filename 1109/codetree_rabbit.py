import heapq

Q = int(input())  # 명령의 수
rabbits = []  # 토끼 리스트
first = list(map(int, input().split()))  # 첫번째 명령
N, M, P = first[1:4]  # N x M 격자, P마리 토끼

for i in range(4, 3 + 2 * P, 2):
    pid, d = first[i:i + 2]  # 각 토끼의 pid(고유번호), d(이동거리)
    # [총 점프 횟수, 행 + 열, 행, 열, 고유번호, 이동거리, 점수]
    # rabbits.append([0, 2, 1, 1, pid, d, 0])
    heapq.heappush(rabbits, [0, 2, 1, 1, pid, d, 0])

for _ in range(Q - 2):  # 첫번째와 마지막 명령을 뺀 나머지 명령들
    play = list(map(int, input().split()))
    if play[0] == 200:  # 경주 진행
        picked = set()  # 뽑힌 토끼 리스트
        for _ in range(play[1]):
            # rabbits.sort(key=lambda x: (x[0], x[1], x[2], x[3], x[4]))
            pick = heapq.heappop(rabbits)
            jump, now, q, p, pid_now, d_now, point = pick  # 최고 우선순위 토끼
            picked.add(pid_now)
            print(pick)
            # 이동할 거리
            dq, dp = d_now % ((N - 1) * 2), d_now % ((M - 1) * 2)

            if dq <= q - 1:
                up = q - dq
            elif dq <= q - 1 + (N - 1):
                up = 1 + dq - (q - 1)
            else:
                up = N - dq + (q - 1) + (N - 1)

            if dq <= N - q:
                down = q + dq
            elif dq <= N - q + (N - 1):
                down = N - dq + (N - q)
            else:
                down = 1 + dq - (N - q) - (N - 1)

            if dp <= p - 1:
                left = p - dp
            elif dp <= p - 1 + (M - 1):
                left = 1 + dp - (p - 1)
            else:
                left = M - dp + (p - 1) + (M - 1)

            if dp <= M - p:
                right = p + dp
            elif dp <= M - p + (M - 1):
                right = M - dp + (M - p)
            else:
                right = 1 + dp - (M - p) - (M - 1)

            # 상, 하, 좌, 우
            move = [[up, p],
                    [down, p],
                    [q, left],
                    [q, right]]
            move.sort(key=lambda x: (-(x[0] + x[1]), -x[0], -x[1]))
            pick[1:4] = (move[0][0] + move[0][1]), move[0][0], move[0][1]
            pick[0] += 1

            for rabbit in rabbits:
                rabbit[6] += pick[1]

            heapq.heappush(rabbits, pick)

        rabbits.sort(key=lambda x: (-x[1], -x[2], -x[3], -x[4]))
        for rabbit in rabbits:
            if rabbit[4] in picked:
                rabbit[6] += play[2]
                break

    else:  # 이동거리 변경
        for rabbit in rabbits:
            if rabbit[4] == play[1]:
                rabbit[5] *= play[2]
                break

last = input()
rabbits.sort(key=lambda x: -x[6])
print(rabbits[0][6])
