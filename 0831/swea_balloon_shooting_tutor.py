def shoot(idx):
    global balloons
    global dead
    global cnt
    global ans
    global sum
    global N
    # 종료 조건 -> N개의 총알을 다 쐇으면 (N개의 풍선이 모두 터졌으면)
    if cnt == N:
        ans = max(sum, ans)  # 최대값 갱신
        return

        # backtracking / 가지치기 -> 현재 idx번 풍선이 터진 풍선이라면
    if dead[idx] == 1:
        return  # 바로 돌아가기

    left = -1
    right = -1
    # 왼쪽에 풍선이 있는지 확인
    for i in range(idx - 1, -1, -1):
        # 살아있는 풍선이라면 -> 여기가 이제 현재 idx번 풍선의 왼쪽에 있는 풍선
        if dead[i] == 0:
            left = i
            break
            # 오른쪽에 풍선이 있는지 확인
    for i in range(idx + 1, N):
        # 살아있는 풍선이라면 -> 여기가 현재 idx번 풍선의 오른쪽에 있는 풍선
        if dead[i] == 0:
            right = i
            break

    temp = 0  # 임시 변수 - 나중에 돌아왔을때 차감해야 할 점수를 담는다.
    # 양쪽에 풍선이 있다면 -> 인접한 두 풍선의 곱을 점수로 더함
    if left != -1 and right != -1:
        temp = balloons[left] * balloons[right]
        # 왼쪽에만 풍선이 있다면 -> 왼쪽 풍선의 값을 점수로 더함
    elif left != -1 and right == -1:
        temp = balloons[left]
        # 오른쪽에만 풍선이 있다면 -> 오른쪽 풍선의 값을 점수로 더함
    elif left == -1 and right != -1:
        temp = balloons[right]
    # 둘다 없다면 = 마지막 풍선 -> 현재 위치의 풍선의 값을 점수로 더함
    else:
        temp = balloons[idx]
    sum += temp  # 이번 라운드의 점수를 누적
    dead[idx] = 1  # idx번 풍선이 터진다
    cnt += 1  # 한개의 풍선이 더 터졌다

    # 다음 풍선을 터트리러 가본다
    # 이미 터진 풍선은 위의 backtracking 부분에서 처리 O(1)
    for i in range(N):
        shoot(i)
        # 다시 돌아왔을 때 -> 이번에 터졌던 풍선 복구
    sum -= temp
    dead[idx] = 0
    cnt -= 1


T = int(input())
for tc in range(1, T + 1):
    # reset
    cnt = 0
    ans = -21e8
    sum = 0
    # input
    N = int(input())
    balloons = list(map(int, input().split()))
    dead = [0 for _ in range(N)]
    # solve
    for i in range(N):
        shoot(i)
    # output
    print(f"#{tc} {ans}")
