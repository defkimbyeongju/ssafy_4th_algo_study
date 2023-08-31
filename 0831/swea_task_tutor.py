def func(idx):
    global flag
    # cycle이 발생했다 -> 처리가 불가능한 업무의 순환이다
    if flag == 1:
        return -1
        # idx번 업무에 대해 처리가 이미 되었다면 다시 들어가지 말고 정답을 return
    if dp[idx] != 0:
        return dp[idx]
        # 만약 하위 업무가 없다면 -> dp에 기록하고 return
    if len(pre[idx]) == 0:
        dp[idx] = worktime[idx]
        return dp[idx]

    maxtime = 0
    # idx번 업무에 연결된 하위 업무들을 확인
    for i in range(len(pre[idx])):
        next = pre[idx][i]
        # cycle이 발생했다 -> 처리가 부가능한 업무의 순환이다.
        if visited[next] == 1:
            flag = 1
            return -1
        # 이 업무를 진행한다!
        visited[next] = 1
        # 다음 업무로 들어간다 (하위 업무)
        temp = func(next)
        # next번 업무를 끝내기까지 걸리는 하위 업무들의 최장 기간을 기록
        if temp > maxtime:
            maxtime = temp
            # 복구 (다른 순서로 해결하면 더 빨라질 수도 있으니)
        visited[next] = 0

        # idx업무를 진행하면 하위 업무들을 끝내기 위해 필요한 시간 + idx 번 업무를 끝내는 시간 소요
    dp[idx] = maxtime + worktime[idx]
    return dp[idx]


T = int(input())
for tc in range(1, T + 1):
    # input
    N = int(input())
    worktime = [0]  # 1번 업부무터 넣을수 있도록 일단 0 하나 투입 (의미 없음)
    pre = [[] for _ in range(N + 1)]  # 1~N번까지 그래프 생성
    for i in range(N):
        info = list(map(int, input().split()))  # 정보 한줄 입력
        worktime.append(info.pop(0))  # 맨 앞의 값이 i+1번째 시간
        M = info.pop(0)  # 다음이 i+1번째 업무에 대한 사전 업무들
        for j in range(M):
            prenum = info.pop(0)  # 앞에서부터 순서대로 빼서
            pre[i + 1].append(prenum)  # i + 1번재의 선행 업무로 투입

    # solve
    ans = 21e8
    for i in range(1, N + 1):
        dp = [0 for _ in range(N + 1)]
        flag = 0
        res = 0  # j번 업무까지를 마쳤을때의 시간

        # i번 업무에 코코를 투입
        original = worktime[i]
        worktime[i] //= 2
        for j in range(1, N + 1):
            # j번 업무부터 시작
            visited = [0 for _ in range(N + 1)]
            visited[j] = 1
            # j번 업무의 하위 업무 처리
            temp = func(j)
            # 만약 j번을 처리하는데에 기존 시간보다 더 넘어갔다면 -> 이때까지 업무를 해야 한다 -> 갱신
            if temp > res:
                res = temp
            # 만약 비정상적인 업무 순환이 생긴다면 -> -1
            if flag == 1:
                ans = -1
                break

                # 코코를 투입했던 기존 시간을 복구
        worktime[i] = original
        # 비정상적인 업무 순환 -> -1
        if flag == 1:
            break
            # 최종적으로 i번 업무에 코코를 투입했을때 모든 업무를 끝내기까지의 시간을 갱신 (최소)
        else:
            ans = min(ans, res)
    # output
    print(f"#{tc} {ans}")