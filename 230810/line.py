N = int(input()) # 학생 수 입력 받음
arr = list(map(int, input().split())) # 줄 바꿀 번호 리스트로 입력 받기
idx_list = [i for i in range(1, N+1)] # 학생 번호를 1-N까지 입력 받아서 별도의 리스트로 설정
for i in range(1, N): # 첫번째로 뽑은 학생은 어차피 0을 뽑기 때문에, 2번째 학생부터 시작.
    for j in range(i, i-arr[i], -1): # 뽑은 숫자만큼 반복하며 앞의 학생과 위치 바꾸기
        arr[j-1], arr[j] = arr[j], arr[j-1]
        idx_list[j-1], idx_list[j] = idx_list[j], idx_list[j-1] # 별도로 설정한 학생 번호 리스트도 동일하게 순서를 바꿔주기!

print(*idx_list) # 학생 번호 리스트를 출력하기