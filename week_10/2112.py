# combinations 모듈 불러오기
from itertools import combinations

# 테스트 케이스 개수 입력
T = int(input())
# 각각의 테스트 케이스에 대하여 진행
for tc in range(1, T + 1):
    # 보호 필름의 두께, 가로크기, 합격 기준 입력
    D, W, K = map(int, input().split())
    # 보호 필름 단면의 정보 리스트로 입력
    films = [list(map(int, input().split())) for _ in range(D)]
    # 약품의 최소 투입 횟수 변수 설정
    least_injection = -1

    # 보호 필름의 성능 검사 함수 설정
    def check(injected):
        # 전역 변수 설정
        global D, W, K

        # 각 열에 대하여 진행
        for column in range(W):
            # 연속된 개수 변수 설정
            successive = 1
            
            # 가장 첫 행의 필름 상태 변수 설정
            if injected[0] == -1:
                previous = films[0][column]
            else:
                previous = injected[0]
            
            # 각 행에 대하여 진행
            for row in range(1, D):
                # 현재 행의 필름 상태 변수 설정
                if injected[row] == -1:
                    now = films[row][column]
                else:
                    now = injected[row]
                
                # 이전 필름과 비교 후 연속 상태 확인
                if now == previous:
                    successive += 1
                else:
                    successive = 1
                
                # 테스트를 통과했다면 다음 열로 넘어가기
                if successive == K:
                    break
                # 테스트를 통과하지 못했다면 이전 필름의 상태 최신화
                else:
                    previous = now
            # 한 행에서 테스트를 통과하지 못했다면 실패 반환
            else:
                return False
        # 모든 열에 대하여 테스트를 통과했다면 성공
        else:
            return True

    # injection 만큼 약품을 투입 했을 때 보호 필름의 단면 확인 함수 설정
    def drug(injection):
        # 전역 변수 설정
        global D, K, least_injection
        
        # 최대 투입 횟수까지도 테스트에 통과하지 못했다면 종료
        if injection == K:
            least_injection = K
            return
        
        # 행 중에서 약품을 투입할 injection 개의 행 선택
        rows = [r for r in range(D)]
        for injected_rows in combinations(rows, injection):
            # 선택된 행의 약품 상태 설정
            for case in range(2 ** len(injected_rows)):
                binary_num = list(map(int, (bin(case)[2:])))
                injected = [-1] * D
                index = 0
                for injected_row in injected_rows:
                    injected[injected_row] = 0 if index - len(injected_rows) < - len(binary_num) else binary_num[index - len(injected_rows)]
                    index += 1
                
                # 이번 경우에 테스트를 통과했다면 종료
                if check(injected):
                    least_injection = injection
                    return
        # 이번 투입에 테스트를 통과하지 못했다면 다음 테스트 진행
        else:
            drug(injection + 1)

    # 약품 투입 진행
    drug(0)
    # 약품의 최소 투입 횟수 출력
    print(f"#{tc} {least_injection}")
