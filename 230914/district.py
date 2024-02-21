# 문제 해결 단계
# 1. 가능한 모든 조합을 만든다. ex) [[1], [2,3,4]] ... [[2,4], [1,3]]
# 2. 각 조합이 연결되는지 확인하는 함수 생성
# 3. 연결되었다면 각 그룹의 유권자 수 차이를 계산하는 함수 실행
# 4. for문으로 최소값 갱신

def combinations(arr, n):  # 조합을 만드는 함수
    def backtrack(start, current_combination):
        if len(current_combination) == n:
            not_in_list = []
            for k in arr:
                if k not in current_combination:
                    not_in_list.append(k)
            result.append([current_combination[:], not_in_list])
            return
        for i in range(start, len(arr)): # 첫번째 요소부터 끝까지
            current_combination.append(arr[i])
            backtrack(i + 1, current_combination) # 다음 요소부터 담기 시작
            current_combination.pop()

    result = []
    backtrack(0, [])
    return result

def sum_district(arr): # 각 마을의 유권자 차이를 반환하는 함수
    group_1 = [voters[arr[0][i]] for i in range(len(arr[0]))]
    group_2 = [voters[arr[1][i]] for i in range(len(arr[1]))]

    return abs(sum(group_1) - sum(group_2))

def check_adj(arr):  # 각 마을끼리 인접해 있는지 확인하고 값을 계산해서 최소값 반환
    min_v = 21e8
    for p in range(len(arr)):
        visited = [0] * N
        for i in range(2):
            if len(arr[p][i]) == 1: # 길이가 1이라면 자기 혼자만 포함되기 때문에 방문 표시
                visited[arr[p][i][0]] = 1
            else:
                for j in range(len(arr[p][i])): # arr[p][i] ex) [[0], [1,2,3]] 에서 [1,2,3]
                    for k in range(N): # adj_arr 한 행의 길이는 N이기 때문에
                        if adj_arr[arr[p][i][j]][k] == 1 and visited[k] == 0 and k in arr[p][i]: # 인접 체크가 되어 있고, 아직 방문하지 않았고, k가 같은 그룹에 해당하면
                                visited[k] = 1
        if sum(visited) == N: # visited로 인접 여부 확인
            res = sum_district(arr[p])
            if min_v > res:
                min_v = res
    return min_v


# 예제
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    adj_arr = [list(map(int, input().split())) for _ in range(N)]  # 인접 행렬 입력
    voters = list(map(int, input().split()))  # 마을 별 유권자 수를 입력
    idx_list = [i for i in range(N)] # 각 마을의 인덱스를 리스트로 따로 생성
    min_val = 21e8 # 최소값 초기 설정
    for i in range(1, N//2+1): # ex) (1개,3개) 조합이나 (3개,1개) 조합이 같기 때문에 정확히 절반씩 나누는 지점까지만 반복문 실행.
        result = combinations(idx_list, i) # 가능한 모든 조합 생성
        res = check_adj(result) # 인접한지 확인하고 최소값 반환
        if min_val > res:
            min_val = res
    print(f'#{tc} {min_val}')