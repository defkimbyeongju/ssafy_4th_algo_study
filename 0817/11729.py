N = int(input())
cnt = 0
# 이동을 기록할 리스트
arr = []


# n은 쌓인 원판 개수, s는 현재 위치, e는 옮길 위치, r은 나머지 위치
def hanoi(n, s, e, r):
    global cnt
    # 원판이 하나 남았다면
    if n == 1:
        # 옮겨줍니다
        arr.append([s, e])
        cnt += 1
    else:
        # 아니라면 맨 밑 원판을 뺀 위의 원판들을 나머지 위치(r)로 옮겨줍니다
        hanoi(n-1, s, r, e)
        # 위 원판들 다 옮겼으면 맨 밑 원판을 옮겨줍니다
        arr.append([s, e])
        cnt += 1
        # 옮겨놨던 위 원판들을 맨 밑 원판이 옮겨간 자리로 다시 옮겨줍니다
        hanoi(n-1, r, e, s)


hanoi(N, 1, 3, 2)
print(cnt)
for i in range(len(arr)):
    print(*arr[i])
