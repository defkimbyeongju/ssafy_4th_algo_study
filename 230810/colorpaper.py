N = int(input())  # 색종이 수만큼 입력받기
arr = [[0]*100 for _ in range(100)]  # 최대 길이가 100이기 때문에 100*100 배열 생성
for _ in range(N):
    a, b = map(int, input().split())  # 가로, 세로 좌표 입력 받기
    for i in range(b, b+10):  # 행 먼저 조회, 길이는 10으로 고정되어 있음
        for j in range(a, a+10):  # 열 순회
            arr[i][j] = 1 # 0으로 채워진 리스트에 1 할당해주기
result = [a for item in arr for a in item] # 이중 리스트 풀어주기

print(sum(result))