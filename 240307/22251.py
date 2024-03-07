# 먼저, 0-9에서 다른 숫자로 변경하는데 얼만큼 반전시켜야 하는지 구함
elv = ['1111110', '0110000', '1101101', '1111001', '0110011', '1011011', '1011111', '1110000', '1111111', '1111011']
switch = [[0]*10 for _ in range(10)] # 각 숫자에 대해 몇 번 바꿔야 하는지 체크하는 리스트
for i in range(9):
    for j in range(i+1, 10):
        cnt = 0
        for idx in range(7):
            if elv[i][idx] != elv[j][idx]:
                cnt += 1
        switch[i][j], switch[j][i] = cnt, cnt
print(switch)
n, k, p, x = map(int, input().split())
result = 0
# 최대로 나올 수 있는 층(n)
max_floor = str(n).zfill(k)
# 시작하는 층(x)
start_floor = str(x).zfill(k)

# 백트래킹으로 문제 해결
def find_case(floor, changed, length):
    global result
    if length == k: # 자리수가 다 찼을 때
        if floor <= max_floor and floor != start_floor and int(floor) != 0: # 현재 층이 범위 내에 들어오고, 시작 층이랑 다르며, 0이 아닐 때 1 증가
            result += 1
        return
    else: # 자리수가 다 채워지지 않았을 때
        if floor.ljust(k, "0") > max_floor: # 지금까지 채워진 자리수가 최대층보다 높으면 return
            return
    num = int(start_floor[length])
    for i in range(10):
        if changed + switch[num][i] <= p:
            find_case(floor+str(i), changed+switch[num][i], length+1)
find_case('', 0, 0)
print(result)