import sys
from collections import deque
import copy


# 선수순서를 입력받아 점수를 산출하는 함수
def game(lst):
    full_players = copy.deepcopy(lst)
    # 문제 조건에 따라 생성된 순열에 4번 타자 넣기
    full_players.insert(3, 0)
    full_players = deque(full_players)
    # 점수 저장할 변수
    score = 0

    # 이닝 별 플레이 시작!
    for i in range(N):  # 각 이닝에 대하여
        player_power = power_list[i]    # 해당 이닝의 선수들 성적리스트
        out_cnt = 0     # 아웃카운트
        base1, base2, base3= 0, 0, 0    # 1루, 2루, 3루 상황
        
        # 3아웃 이닝 종료될 때 까지
        while out_cnt < 3:
            player = full_players.popleft() # 선수 등판
            p = player_power[player]        # 해당 선수의 이닝 성적
            if p == 0:  # 삼진 아웃
                out_cnt += 1    # 아웃카운트 1 증가
                full_players.append(player) # 타자 순서 뒤로 다시 넣고 다음 선수
                continue
            else:       # 출루할 경우
                if p == 1:          # 1루타
                    score += base3  # 3루 주자 점수에 추가
                    base3 = base2   # 2루 -> 3루로
                    base2 = base1   # 1루 -> 2루로
                    base1 = 1       # 1루 출루 성공
                
                elif p == 2:        # 2루타       
                    home = base3 + base2    # 홈에 들어온 2루, 3루 주자 수
                    score += home   # 점수에 추가
                    base3 = base1   # 1루 -> 3루로
                    base2 = 1       # 2루 출루 성공
                    base1 = 0       # 1루엔 아무도 없음
                
                elif p == 3:        # 3루타
                    home = base3 + base2 + base1
                    score += home   # 점수에 추가
                    base3 = 1       # 3루 출루 성공
                    base2 = 0       # 2루 아무도 없음
                    base1 = 0       # 1루 아무도 없음
                
                elif p == 4:        # 홈런
                    home = base3 + base2 + base1 + 1
                    score += home   # 점수에 추가
                    base1, base2, base3 = 0, 0, 0   # 1,2,3루 전부 없음
            # 해당 타자 타순 맨뒤로 정렬
            full_players.append(player)
    # 모든 이닝 종료되면 점수 출력
    return score


# 선수순서 짜는 함수 (순열 생성)
def player_order(cnt):
    global max_score
    # 종료조건
    # 숫자 8개 골랐을 때 종료
    if cnt == 8:
        # 완성된 순열 조합으로 게임실행!
        result = game(temp_order)
        # 결과 점수 최대값 갱신
        if result > max_score:
            max_score = result
        return

    for num in players:
        # 가지치기 : 중복된 숫자 제거
        if num in temp_order:
            continue
        # 재귀 들어가기전 로직 -> 경로 저장
        temp_order[cnt] = num
        # 재귀 호출
        player_order(cnt + 1)
        # 돌아온 후 로직 -> 초기화
        temp_order[cnt] = 0


N = int(sys.stdin.readline())    # 이닝 수
power_list = []     # 이닝 별 선수들 성적 기록할 리스트 생성
# 이닝별 성적 기록하기
for _ in range(N):
    inning_power = list(map(int, sys.stdin.readline().split()))
    power_list.append(inning_power)


max_score = -1          # 최대 점수 기록할 변수 생성
players = [1, 2, 3, 4, 5, 6, 7, 8]  # 순열 함수 돌릴 8명
temp_order = [0] * 8    # 생성된 순열 저장할 변수 생성

player_order(0)     # 함수 호출

print(max_score)    # 결과 출력
