T = int(input())


# 회문 함수
# 양 끝의 글자를 비교해 다르면 2를 반환
# 중간에 for 반복문이 끝나지 않는다면 회문이므로 0 반환
def pal(s):
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            return 2
    else:
        return 0


# 유사회문 함수 1
# 양 끝의 글자를 비교하던 중 다른 글자가 있다면
# 왼쪽의 글자를 pop으로 없애줍니다
# 그러고 위의 회문 함수와 같은 방식으로 검사
def psdpal1(s):
    s = list(s)
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            s.pop(i)
            break
    for j in range(len(s) // 2):
        if s[j] != s[len(s) - 1 - j]:
            return 2
    else:
        return 1


# 유사회문 함수 2
# 1과 같은 원리이나 얘는 오른쪽 글자를 없앱니다
def psdpal2(s):
    s = list(s)
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            s.pop(len(s) - 1 - i)
            break
    for j in range(len(s) // 2):
        if s[j] != s[len(s) - 1 - j]:
            return 2
    else:
        return 1


for _ in range(T):
    string = input()
    # 회문 검사
    ans = pal(string)
    # 회문이 아니라면 유사회문 검사 1
    if ans == 2:
        ans = psdpal1(string)
    # 또 아니라면 유사회문 검사 2
    if ans == 2:
        ans = psdpal2(string)
    print(ans)
