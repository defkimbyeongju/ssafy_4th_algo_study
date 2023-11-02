def move(dt):
    # 반환할 리스트
    new = dict()
    # 현재 위치 값들(키 리스트)
    keys = list(dt.keys())
    # 여러 미생물 군집이 합쳐진 위치를 저장할 리스트
    many = []
    for key in keys:
        # 세로위치, 가로위치
        p, q = key
        # 미생물 수, 이동방향
        n, direc = dt[key]
        # 이동방향에 따라 위치 변경
        if direc == 1:
            p -= 1
        elif direc == 2:
            p += 1
        elif direc == 3:
            q -= 1
        elif direc == 4:
            q += 1
        # 바뀐 위치가 가장자리일 때 처리
        if p in (0, N-1) or q in (0, N-1):
            n[0] //= 2
            direc = reverse[direc]
        # 새 리스트에 없다면 == 아직 안 간 위치
        if not new.get((p, q)):
            new.setdefault((p, q), [n, direc])
        # 누가 이미 있다면
        else:
            # 현재 들어있는 미생물들보다 클 때 이동방향 갱신
            if n[0] > max(new[(p, q)][0]):
                new[(p, q)][1] = direc
            # 미생물 수 넣어주기
            new[(p, q)][0].append(n[0])
            # 여러 군집이 합쳐졌으므로 리스트에 넣기
            many.append((p, q))
    # 여러 군집이 모인 위치는
    for m in many:
        # 미생물 수 리스트를 다 더한 값으로 갱신
        new[m][0] = [sum(new[m][0])]

    return new


T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    # 위치를 딕셔너리로 표현함
    location = dict()
    for _ in range(K):
        y, x, num, d = map(int, input().split())
        # {(1, 1): [[7], 1], (2, 1): [[7], 1], ...}
        location.setdefault((y, x), [[num], d])
    # 가장자리에서 이동방향 반대로 바꿔줄 리스트
    reverse = [0, 2, 1, 4, 3]
    for _ in range(M):
        location = move(location)
    # 각 위치의 미생물 수 더해줌
    ans = 0
    for value in list(location.values()):
        ans += value[0][0]
    print(f'#{tc}', ans)