# 직사각형이 차지하는 부분
occupied = set()

# 네 줄 입력 받기
for _ in range(4):
    left_bottom_x, left_bottom_y, right_top_x, right_top_y = map(int, input().split())

    # 직사각형의 단위 정사각형 세트 안에 넣기
    for y in range(left_bottom_y, right_top_y):
        for x in range(left_bottom_x, right_top_x):
            occupied.add((x, y))

# 네 개의 직사각형이 차지하는 면적 출력
print(len(occupied))
