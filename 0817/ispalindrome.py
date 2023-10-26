def is_palindrome(s):
    return s == s[::-1]


def is_pseudo_palindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            # Try removing character from the left or right side
            left_removed = s[:i] + s[i + 1:]
            right_removed = s[:len(s) - i - 1] + s[len(s) - i:]

            if is_palindrome(left_removed) or is_palindrome(right_removed):
                return True
            else:
                return False
    return True


def classify_string(s):
    if is_palindrome(s):
        return 0
    elif is_pseudo_palindrome(s):
        return 1
    else:
        return 2


# 입력 처리
T = int(input())  # 테스트 케이스 개수 입력
for _ in range(T):
    string = input()  # 문자열 입력
    result = classify_string(string)  # 문자열 분류
    print(result)  # 결과 출력


'''
def ispalindrome(txt):
    if txt == txt[::-1]:
        return 0
    else:
        k = len(txt)
        for i in range(k//2):
            if not txt[i] == txt[k-i-1]:
                if txt[i] == txt[k-i-2]:
                    del txt[k-i-1]
                    if txt == txt[::-1]:
                        return 1
                    else:
                        return 2
                elif txt[i-1] == txt[k-i-1]:
                    del txt[i]
                    if txt == txt[::-1]:
                        return 1
                    else:
                        return 2
                else:
                    return 2
        return 2

n = int(input())
for _ in range(n):
    txt = list(input())
    print(ispalindrome(txt))
'''