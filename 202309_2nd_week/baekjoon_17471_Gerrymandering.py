import copy
# 중복되니까 절반만
def BFS(start, lst):
    visited = [0] * N
    Q = []
    Q.append(start)
    visited[start] = 1
    while Q:
        now = Q.pop(0)
        for i in range(N):
            if not visited[i] and tmp_arr[now][i] == 1:
                Q.append(i)
                visited[i] = 1
    # 해당 선거구 안이 모두 연결되었는지 확인
    for i in lst:
        if not visited[i]:  # 연결되지 않은 마을 있으면
            return False    # False 리턴
    return True             # 문제없으면 True 리턴



N = int(input())
voters = list(map(int, input().split()))    # 마을별 유권자 수
arr = [[0] * N for _ in range(N)]   # 마을 연결상태를 입력할 arr 생성
for i in range(N):
    info = list(map(int, input().split()))  # 각 마을별 연결정보
    for j in range(info[0]):
        arr[i][info[j+1] - 1] = 1   # 연결되어 있는 마을이면 정보 갱신

towns = list(range(N))  # 마을 리스트
result = float('inf')   # 최소값 저장할 변수

# 백준시를 두 선거구로 나누는 부분집합 구하기
for i in range(1, 1 << (N - 1)):  # 1<<(N-1) == (1<<N)//2
    area1 = []
    area2 = []
    for j in range(N):
        if i & (1 << j):  # j번 비트가 0이 아니면
            area1.append(towns[j])
        else:
            area2.append(towns[j])
    # 각 경우의 수를 체크하기 위해 임시배열 복사
    tmp_arr = copy.deepcopy(arr)
    # 동일 선거구가 아니면 마을 간 연결 해제
    for n in area1:
        for m in area2:
            tmp_arr[n][m] = 0
            tmp_arr[m][n] = 0
    # 각 선거구 별 유권자 수 초기화
    voter1 = 0
    voter2 = 0
    # 문제없이 두 선거구로 나뉘었다면
    if BFS(area1[0], area1) and BFS(area2[0], area2):
        # 각 선거구 별 유권자 수 구하기
        for k in area1:
            voter1 += voters[k]
        for l in area2:
            voter2 += voters[l]
        # 유권자 수 차이 구하기
        ans = abs(voter1 - voter2)
        # 최솟값 구하기
        if ans < result:
            result = ans
# 문제없이 선거구를 연결할 수 있는 방법이 없다면
if result == float('inf'):
    result = -1     # 결과값은 -1
print(result)       # 결과 출력
