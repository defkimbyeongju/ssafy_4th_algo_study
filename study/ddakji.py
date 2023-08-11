# 딱지문제
N = int(input())
for _ in range(N): # N번 반복
    A = [[0]*5 for _ in range(2)]  # 0으로 채워진 리스트 생성
    arr = [] # 빈 리스트 생성
    for i in range(2):
        arr.append(list(map(int,input().split())))  # 입력 값을 이중리스트로 받음

    for j in range(2):
        for k in range(1, arr[j][0]+1):
            A[j][arr[j][k]] += 1  # 0으로 채워진 리스트에 4,3,2,1 중 해당 값이 나올때마다 1씩 인덱스로 추가

    for i in range(4, 0, -1):  # 가장 강력한 별에 해당하는 4부터 1까지 반복하며 개수 비교
        if A[0][i] > A[1][i]:
            print('A')
            break
        elif A[0][i] < A[1][i]:
            print('B')
            break
        if i == 1: # 마지막까지 돌았는데도 개수가 모두 똑같을 때는 Draw
            if A[0][1] == A[1][1]:
                print('D')
                break
