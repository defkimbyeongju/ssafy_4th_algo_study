def recur(n, q1, q2):
    global answer
    if n == length:
        # 0부터 n까지 쌓였을 때 result값 계산
        q1.sort()
        q2.sort()
        result = 0

        for i, x in enumerate(q1):
            if 0 <= i-3 and x <= q1[i-3]+s1:
                result = max(result, q1[i-3]+2*s1+1)
                # 3명 이상 기다린다면 3명 이후부터는
            else:
                result = max(result, x+s1+1)
                # 3명 이하라면

        for i, x in enumerate(q2):
            if 0 <= i-3 and x <= q2[i-3]+s2:
                result = max(result, q2[i-3]+2*s2+1)
                # 3명 이상 기다린다면 3명 이후부터는
            else:
                result = max(result, x+s2+1)
                # 3명 이하라면
                
        answer = min(answer, result)    # 최소값 업데이트
        return
    r, c = people[n]
    recur(n+1, q1+[abs(sr1-r)+abs(sc1-c)], q2)
    recur(n+1, q1, q2+[abs(sr2-r)+abs(sc2-c)])
    # n번째 사람에서 q 업데이트
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    INF = N*N+10
    matrix = [list(map(int, input().split())) for _ in range(N)]
    people = []
    sr1, sc1, s1, sr2, sc2, s2 = None, None, None, None, None, None
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
    answer = 987654321
    recur(0, [], [])
    print(f'#{tc} {answer}')