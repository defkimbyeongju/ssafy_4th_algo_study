# 색종이 붙은 부분
occupied = set()

# 색종이의 수
N = int(input())

# 색종이 수만큼 반복
for _ in range(N):
    left_bottom_x, left_bottom_y = map(int, input().split())

    # 색종이가 붙는 부분의 단위 정사각형 세트 안에 넣기
    for dy in range(10):
        for dx in range(10):
            occupied.add((left_bottom_x + dx, left_bottom_y + dy))

# 넓이 출력
print(len(occupied))
