arr = [[0] * 100 for _ in range(100)] # 2차원 리스트로 0을 x,y의 최대값인 100*100으로 만들어줌

for _ in range(4): # 입력이 4번 있기 때문에 4번 반복으로 범위 설정
    a, b, c, d = map(int, input().split()) # (a,b), (c,d) 두 개의 좌표를 각각 따로 변수에 설정하여 입력받음
    for i in range(b, d): # arr의 인덱스로 접근하여 해당 위치에 값을 1로 바꾸려고 한다. y좌표가 행이기 때문에 행에 해당하는 b,d를 for문으로 묶어줌
        for j in range(a, c): # x좌표 값에 해당하는 a부터 c까지 반복
            arr[i][j] = 1 # 해당 위치 값을 1로 변경

list2 = [data for inner_list in arr for data in inner_list]

print(sum(list2))


# 망한 접근
# for _ in range(4):
#     arr.append(list(map(int, input().split())))
# area = (arr[0][2] - arr[0][0]) * (arr[0][3] - arr[0][1])
# comma = []
# for i in range(4):
#     y, x = arr[i][0], arr[i][2]
#     z, w = arr[i][1], arr[i][3]
#     for j in range(y, x+1):
#         for k in range(z, w+1):
#             comma.append((j, k))
# comma = list(set(comma))
