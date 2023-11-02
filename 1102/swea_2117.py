def service(n):
    # 마름모 모양을 만들 함수
    area = []
    for j in range(n):
        for i in range(-(n - 1) + j, n - j):
            area.append((i, j))  # 오른쪽 끝
            area.append((i, -j))  # 왼쪽 끝
    return list(set(area))
    # return 값은 [(0, 0), (-1, 0), (1, 0), (0, 1), (0, -1)] 이런식


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = 0
    for k in range(1, N + 1 - (N % 2) + 1):  # 범위는 넉넉하게 잡기
        direct = service(k)
        for p in range(N):
            for q in range(N):
                cnt = 0
                for di, dj in direct:  # 마름모 모양 확인하기
                    ni, nj = p + di, q + dj
                    if 0 <= ni < N and 0 <= nj < N:  # 도시 안에 있고
                        if arr[ni][nj]:  # 집이면
                            cnt += 1
                # 손해만 안보면 되므로 0 이상
                if (cnt * M) - len(direct) >= 0:
                    if max_cnt < cnt:
                        max_cnt = cnt
    print(f'#{tc}', max_cnt)
