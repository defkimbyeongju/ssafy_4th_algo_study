# 유사회문 여부인지를 판단하는 함수
def pseudo(word):
    return 1 if word == word[::-1] else 2   # 역슬라이싱 한것과 같으면 회문이므로 1 리턴

# 회문 여부 판별 함수
def palindrome(word):
    n = len(word)
    for i in range(n // 2 + n % 2):     # 중복체크를 막기 위해 문자열의 절반까지 체크
        if word[i] != word[-1 - i]:     # 만약 회문이 아니라면
            new_word = word[:i] + word[i + 1:]  # 앞의 문자가 문제인 경우
            new2_word = word[:n - 1 - i] + word[n - i:] # 뒤의 문자가 문제인 경우
            # 오류문자를 제외한 새 문자열이 유사회문인지를 판별
            if pseudo(new_word) == 1 or pseudo(new2_word) == 1:
                return 1    # 앞이나 뒤문자 제거후 유사회문 맞으면 1 리턴
            return 2        # 둘다 회문이 아니라면 2 리턴
    return 0                # 아무 문제 없으면 완전한 회문으로 0 리턴

# 함수 호출
T = int(input())
for tc in range(T):
    string = input()
    print(palindrome(string))
