def recur(n, q1, q2):
    # 현재 처리 중인 사람의 인덱스 / 계단1 큐 / 계단2 큐
    global answer
    if n == length:
        q1.sort()
        q2.sort()
        result = 0
        # n이 사람 수에 도달하면, 두 개의 큐를 정렬
        # result는 0으로 초기화

        # 첫 번째 큐에 대한 도착 시간 계산
        for i, x in enumerate(q1):
            if 3 <= i and x <= q1[i-3]+s1:
                result = max(result, q1[i-3]+2*s1+1)
                # 3명 이상 기다리고 있다면 
                # 3명 이전의 사람이 계단을 이용한 후 도착한 시간 (q1[i-3]) 
                # + 3명 사람들 간의 간격 (2*s1) 
                # + 대기시간 (1)
            else:
                result = max(result, x+s1+1)
                # 3명 이하라면 현재 계단 이용
                # 도착 시간 (x) 
                # + 계단을 내려가는 시간 (s1) 
                # + 대기시간 (1)

        # 두 번째 큐에 대한 도착 시간 계산
        for i, x in enumerate(q2):
            if 0 <= i-3 and x <= q2[i-3]+s2:
                result = max(result, q2[i-3]+2*s2+1)
            else:
                result = max(result, x+s2+1)

        answer = min(answer, result)
        # q1과 q2의 도착 시간 중에서 가장 큰 값을 선택하여 할당한 result값을
        # answer와 비교하여 더 작은 값을 answer에 업데이트
        return
    
    r, c = people[n]
    recur(n+1, q1+[abs(sr1-r)+abs(sc1-c)], q2)
    recur(n+1, q1, q2+[abs(sr2-r)+abs(sc2-c)])
    # 현재 사람의 인덱스와 큐를 업데이트하여 재귀 호출
    # 다음 사람의 도착 시간 계산 후 q의 끝에 업데이트
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    people = []
    sr1, sc1, s1, sr2, sc2, s2 = None, None, None, None, None, None
    # 두 계단의 좌표와 계단의 길이 저장
    for r in range(N):
        for c in range(N):
            if not matrix[r][c]: continue
            elif matrix[r][c] == 1:
                people.append((r,c))
            else:
                if sr1 is None:
                    sr1, sc1, s1 = r, c, matrix[r][c]
                else:
                    sr2, sc2, s2 = r, c, matrix[r][c]
 
    length = len(people)
    answer = 100000*1000000000
    recur(0, [], [])
    print(f'#{tc} {answer}')