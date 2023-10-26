# 테스트 케이스 개수 입력
T = int(input())
# 각각의 테스트 케이스에 대하여 진행
for tc in range(1, T + 1):
    # 숫자의 개수와 크기 순서 입력
    N, K = map(int, input().split())
    # 16진수 숫자 리스트로 입력
    treasure = input()

    # 보물상자의 크기 T 설정
    T = len(treasure)
    # 한 변의 길이 S 설정
    S = T // 4
    # 보물상자에 적힌 숫자로 만들 수 있는 수를 담을 세트 설정
    numbers = set()
    
    # 각 회전에 대하여
    for rotate in range(S):
        # 각 변에 대하여
        for side in range(4):
            # 이 변의 숫자 확인 및 numbers 에 추가
            side_number = ""
            for index in range(side * S, (side + 1) * S):
                side_number += treasure[index - rotate]
            side_number = int(side_number, 16)
            numbers.add(side_number)

    # K 번째로 큰 수 출력
    print(f"#{tc} {sorted(numbers, reverse=True)[K - 1]}")
