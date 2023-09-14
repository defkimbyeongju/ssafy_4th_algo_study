N, K = map(int,input().split()) # 학생 수, 방 최대 수용인원 입력 받기
count = 0 # 방 개수를 세기 위한 카운트
arr = [[0]*6 for _ in range(2)]  # 여학생, 남학생 구분할 이중 리스트를 만들어준다
for _ in range(N): # 학생 수 만큼 반복
    a, b = map(int, input().split()) # 성별, 학년 입력 받기
    arr[a][b-1] += 1 # 성별은 0, 1이고, 학년은 1,2,3,4,5,6. 해당 위치에 1씩 증가

for i in range(2): # 성별만큼
    for j in range(6): # 학년만큼
        count += (arr[i][j]//K) # 각 성별-학년별 인원을 모두 순회하며, 방 최대인원으로 나눴을 때 그 몫만큼 개수 세기
        if arr[i][j] % K != 0: # 만약 방 최대수용인원으로 나눴을 때 나머지가 생긴다면 모두 방 1개에 넣으면 되니까 1씩 추가해주기
            count += 1
print(count)
