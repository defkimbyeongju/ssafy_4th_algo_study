# copy 모듈 불러오기
import copy

# 테스트 케이스 입력
T = int(input())
# 각 테스트 케이스마다 진행
for tc in range(1, T + 1):
    # 업무의 개수 입력
    N = int(input())
    # 업무의 정보 리스트로 입력
    original = [list(map(int, input().split())) for _ in range(N)]
    # 모든 업무를 완료하기 위해 필요한 최소 소요시간 설정
    min_work_time = 1000 * N + 1

    # 각각의 업무를 코코가 도와줄 경우에 대하여 진행
    for idx in range(N):
        # 업무 소요 시간 설정
        work_time = 0
        # 코코가 도와준 업무는 소요 시간을 절반으로 하는 새로운 업무의 정보 리스트 설정
        work_info_list = copy.deepcopy(original)
        work_info_list[idx][0] //= 2
        # 아직 완료되지 않은 업무는 0, 완료된 업무는 -1, 진행중인 업무는 1로 표현하는 작업 상태 리스트 설정
        can_start_list = [0] * N

        # 업무 진행
        while True:
            # 이번 작업시 최소 소요 시간 설정
            least_time = 1001
            # 새로운 업무의 정보 리스트 순회하며 진행
            for work_info_idx in range(N):
                # 사전 업무를 보유하고 있다면
                if work_info_list[work_info_idx][1] > 0:
                    # 각각의 사전 업무에 대하여
                    for pre_work in work_info_list[work_info_idx][2:]:
                        # 사전 업무가 완료되지 않았다면
                        if can_start_list[pre_work - 1] != -1:
                            # 이번에도 해당 업무는 진행 불가능
                            break
                    # 사전 업무가 완료되었다면
                    else:
                        # 새로운 업무의 정보 리스트 최신화 -> 사전 업무 내용을 제외
                        work_info_list[work_info_idx] = [work_info_list[work_info_idx][0], 0]
                        # 이번 작업 진행 시의 최소 시간인지 확인
                        least_time = min(least_time, work_info_list[work_info_idx][0])

                # 사전 업무를 보유하지 않고 완료되지도 않았다면
                if work_info_list[work_info_idx][1] == 0 and work_info_list[work_info_idx][0] != 0:
                    # 작업 상태 리스트 최신화 -> 진행중으로 표기
                    can_start_list[work_info_idx] = 1
                    # 이번 작업 진행시의 최소 시간인지 확인
                    least_time = min(least_time, work_info_list[work_info_idx][0])

            # 만약 위의 과정에서 아무 변화도 있지 않았다면
            if least_time == 1001:
                # 작업 종료
                break
            # 이번 작업 진행시의 최소 시간만큼 업무 시간에 추가
            else:
                work_time += least_time

            # 진행중인 작업에 대하여 최소 시간 업무 진행
            for can_start_work_idx in range(N):
                if can_start_list[can_start_work_idx] == 1:
                    work_info_list[can_start_work_idx] = [work_info_list[can_start_work_idx][0] - least_time, 0]
                    # 이번 과정에서 작업이 종료되었다면
                    if work_info_list[can_start_work_idx][0] == 0:
                        # 작업 상태 리스트 최신화 -> 완료된 업무로 표기
                        can_start_list[can_start_work_idx] = -1

        # 진행 완료되지 않은 작업이 없다면
        if 0 not in can_start_list:
            # 모든 업무를 완료하기 위해 필요한 최소 소요시간인지 확인
            min_work_time = min(min_work_time, work_time)
        # 진행 완료되지 않은 작업이 있다면
        else:
            # 작업 종료
            break

    # 모든 업무를 완료할 수 없다면
    if min_work_time == 1000 * N + 1:
        print(f"#{tc} -1")
    # 모든 업무를 완료할 수 있다면 필요한 최소 소요시간 출력
    else:
        print(f"#{tc} {min_work_time}")
