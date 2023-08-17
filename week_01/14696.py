# 승자 판별 함수
def winner(a_card_list, b_card_list, shape):
    if shape < 1:
        return "D"
    else:
        if a_card_list.count(shape) > b_card_list.count(shape):
            return "A"
        elif a_card_list.count(shape) < b_card_list.count(shape):
            return "B"
        else:
            return winner(a_card_list, b_card_list, shape - 1)


# 총 라운드 수 입력
N = int(input())

# 각 라운드 진행
for _ in range(N):
    # 길이 제외 딱지 리스트 입력
    a_cards = list(map(int, input().split()))[1:]
    b_cards = list(map(int, input().split()))[1:]

    # 경기 결과 출력
    print(winner(a_cards, b_cards, 4))
