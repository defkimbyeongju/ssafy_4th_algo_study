from itertools import combinations


def film(tp, level, array):
    # level은 부분집합의 인덱스가 될 인자
    if level == len(tp):
        # 세로 방향으로 확인할 것
        for p in range(W):
            prev = array[0][p]  # 초기값 = 맨 위의 값
            cnt = 1  # 연속 카운트
            for q in range(1, D):
                now = array[q][p]
                if now == prev:  # 같으면 카운트 올려주기
                    cnt += 1
                else:  # 다르면 초기화
                    cnt = 1
                prev = now  # 갱신
                if cnt == K:  # K개 만큼 연속되었다면 바로 탈출
                    break
            else:
                # 탈출을 못했다 == K개 만큼 연속되지 않는다
                # 더 검사할 필요 없이 False 반환
                return False
        else:
            # 중간에 False 반환 안되고 모든 열을 다 돌았다
            # 더 볼 필요 없이 해당 부분집합의 개수가 답
            print(f'#{tc}', len(tp))
            # True 반환
            return True
    # 투약할 행을 저장해두고
    save = array[tp[level]]
    # A로 바꿔주기
    array[tp[level]] = [0] * W
    # 재귀의 끝에서 True가 반환된다면 계속 True 반환
    if film(tp, level + 1, array):
        return True
    # B로 바꿔주기
    array[tp[level]] = [1] * W
    # 재귀의 끝에서 True가 반환된다면 계속 True 반환
    if film(tp, level + 1, array):
        return True
    # 원복
    array[tp[level]] = save


T = int(input())
for tc in range(1, T+1):
    D, W, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(D)]
    # 행들의 부분집합 만들기
    nums = [n for n in range(D)]
    subsets = []
    for k in range(D + 1):
        # 원소의 개수(0개 ~ D개) 순서대로 리스트에 추가
        subsets += list(combinations(nums, k))
    # subsets = [(), (0), (1), ... , (0, 1), (0, 2), ...]
    for subset in subsets:
        # 각 부분집합마다 함수 실행
        if film(subset, 0, arr):  # True가 반환됨 == 검사 통과
            break  # 끝냄
