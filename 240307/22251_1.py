# N 층까지있음
# K 자리수
# P 반전
# X 층에 멈춰있음

# 반전 가능한 경우의 수

max_floor, digit_len, twist, X = map(int, input().split())
count = 0

num_dic = {
  "0" : "1110111",
  "1" : "0010010",
  "2" : "1011101",
  "3" : "1011011",
  "4" : "0111010",
  "5" : "1101011",
  "6" : "1101111",
  "7" : "1010010",
  "8" : "1111111",
  "9" : "1111011"
}


def fill_zero(floor):
  floor = str(floor)
  return ('0' * (digit_len - len(floor))) +  floor

def trans_digit(floors):
  current_floor_digit = []
  for i in floors:
    current_floor_digit.append(num_dic[i])
  return current_floor_digit
  
current_floor = fill_zero(X)
current_floor = trans_digit(current_floor)

for check_floor in range(1, max_floor + 1):
  check_floor = fill_zero(check_floor)
  check_floor = trans_digit(str(check_floor))
  if current_floor == check_floor:
    continue
  diff = 0

  for i in range(digit_len):
    for j in range(7):
      if current_floor[i][j] != check_floor[i][j]:
        diff += 1

    if diff > twist:
      break
  else:
    count += 1

print(count)