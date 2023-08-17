# 테스트 케이스 개수 입력
T = int(input())

# 각각의 테스트 케이스에 대하여 진행
for tc in range(T):
    # 문자열 입력
    string = input()

    # 회문인 경우
    if string == string[::-1]:
        print(0)
    else:
        # 문자열 좌우로 살펴가며(백트래킹으로 인덱스 무관)
        for idx in range(len(string)):
            # 회문이 아닌 경우 발견
            if string[idx] != string[len(string) - idx - 1]:
                left = string[:idx] + string[idx + 1:]
                right = string[:len(string) - idx - 1] + string[len(string) - idx:]
                # 유사회문인 경우
                if left == left[::-1] or right == right[::-1]:
                    print(1)
                    break
                # 둘 다 해당되지 않는 경우
                else:
                    print(2)
                    break
