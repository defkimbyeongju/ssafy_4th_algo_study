def check():
    for j in range(W):
        # 필름의 각 열을 반복
        check = False
        for i in range(0,D-K+1):
            # 각 열에 대해 필름의 부분을 수직으로 반복 검사
            s = sum([film[_][j] for _ in range(i, i+K)])
            # 매 i당 합격기준의 길이만큼 더해 합한 값이  
            if not s or s==K:
                check = True
                break
            # 0이나 K가 된다면 통과
        if not check:
            return 0
            # 품질 기준을 충족하지 않는 열이 있다면 바로 0 리턴
    return 1
    # 모든 열이 품질 기준을 충족한다면 그대로 1을 리턴
            
def DFS(row, count):
    # 현재 행 / 현재까지 수행한 작업 수
    global result
    if count >= result:
        return
    # 현재 상태의 task값이 최소값인 result보다 크거나 같으면 더 탐색하지 않음
    if check():
        result = min(result, count)
        return
    # 조건을 만족하면 result값을 최소값으로 업데이트
    for j in range(row, D):
        # 나머지 행 중에서
        c = film[j][:]
        # 원래의 열
        for c in [[0]*W, [1]*W]:
            # 약품 A투입, 약품 B투입
            film[j] = c
            # 약품 A를 투입했을 때와 B를 투입했을 때 각각의 경우에서
            DFS(j+1, count+1)
            # 다음 경로 탐색
        film[j] = c
        # 원래의 열로 되돌리기

T = int(input())
for tc in range(1, 1+T):
    D, W, K =  map(int, input().split())
    # 보호필름의 두께 / 가로크기 / 합격기준 저장
    film = [list(map(int, input().split())) for _ in range(D)]
    # 필름의 형태 저장
    result = D
    # 초기값 D로 설정
    DFS(0,0)
    print(f'#{tc} {result}')
