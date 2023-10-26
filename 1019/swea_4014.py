def f(ground):
    on_runway = False  # 현재 활주로인지 아닌지
    cnt = 1  # 연속으로 같은 높이인 길이
    i = 1  # 인덱스
    while i < N:  # 배열의 길이
        prev = ground[i - 1]  # 이전 위치
        now = ground[i]  # 현재 위치
        if abs(now - prev) > 1:  # 차이가 1보다 크다면 끝
            return False
        if not on_runway:  # 현재 활주로가 아닐 때
            if now == prev:  # 둘이 높이가 같으면
                cnt += 1  # 카운트 올려주고 진행
                i += 1
            elif now - prev == 1:  # 현재 위치가 1만큼 높다면
                if cnt < X:  # 낮은 쪽에 활주로가 지어지는데(이전 위치의 높이에)
                    return False  # 그 높이의 길이가 X보다 작다면 활주로를 못 지으니까 끝
                else:  # X보다 크거나 같다면 활주로 건설 가능
                    cnt = 1  # 활주로 지었으니까 cnt 갱신
                    i += 1
            elif now - prev == -1:  # 현재 위치가 1만큼 낮다면
                on_runway = True  # 활주로 시작
                cnt = 1  # cnt 갱신
                i += 1
        else:  # 현재 활주로일 때
            if now == prev:  # 둘이 높이가 같으면
                cnt += 1  # 카운트 올려주고 진행
                i += 1
            else:  # 현재 활주로인데 높이가 달라진다?
                return False  # 끝
            if cnt == X:  # 활주로 길이가 X랑 같아지면
                on_runway = False  # 활주로 끝
                cnt = 0  # cnt 갱신
    # 배열 다 돌음
    if not on_runway:
        return True
    else:  # 마지막 인덱스에서 활주로 건설중이면 안 됨
        return False


T = int(input())
for tc in range(1, T+1):
    N, X = map(int, input().split())
    columns = [[] for _ in range(N)]  # 열 정보를 받을 2차원 리스트
    ans = 0
    for _ in range(N):
        row = list(map(int, input().split()))  # 행 입력
        if f(row):  # 행에 대해서 확인
            ans += 1
        for x in range(N):  # 각 열에 각 높이 입력
            columns[x].append(row[x])
    for column in columns:
        if f(column):  # 열 확인
            ans += 1
    print(f'#{tc}', ans)
