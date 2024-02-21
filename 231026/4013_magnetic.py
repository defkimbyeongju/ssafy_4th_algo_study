def rotation(lst, dir):
    if dir == 1: # 시계방향
        a = lst.pop()
        lst.insert(0, a)
    else:
        a = lst.pop(0)
        lst.append(a)
    return lst
def func(i, dir): # i: 인덱스, dir은 방향
    temp = []
    d = 1
    for j in range(3):
        if arr[j][2] != arr[j+1][6]:
            temp.append(-1)
        else:
            temp.append(1)
    arr[i] = rotation(arr[i], dir)
    if i == 0: # 첫번째 자석일 때
        for j in range(3):
            if temp[j] == 1:
                break
            dir *= (-1)
            arr[j+1] = rotation(arr[j+1], dir)
    elif i == 3: # 맨 끝에 있을 경우
        for j in range(2,-1,-1):
            if temp[j] == 1:
                break
            dir *= (-1)
            arr[j] = rotation(arr[j], dir)
    elif i == 1:
        if temp[0] == -1: # 왼쪽 갑니다
            arr[0] = rotation(arr[0], dir*(-1))
        for j in range(1, 3): # 오른쪽 갑니다
            if temp[j] == 1:
                break
            dir *= (-1)
            arr[j+1] = rotation(arr[j+1], dir)
    elif i == 2:
        if temp[2] == -1: # 오른쪽 갑니다
            arr[3] = rotation(arr[3], dir*(-1))
        for j in range(1,-1,-1): # 왼쪽으로 갑니다
            if temp[j] == 1:
                break
            dir *= (-1)
            arr[j] = rotation(arr[j], dir)


T = int(input())
for tc in range(1,T+1):
    K = int(input()) # 총 회전 수
    arr = [list(map(int, input().split())) for _ in range(4)]
    total = 0
    for _ in range(K):
        magnetic_num, direction = map(int, input().split())
        func(magnetic_num-1, direction)
    for i in range(4):
        total += arr[i][0] * (2**i)
    print(f'#{tc} {total}')
