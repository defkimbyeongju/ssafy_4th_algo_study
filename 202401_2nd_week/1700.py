# 백준 1700번. 멀티탭 스케줄링

# N = 멀티탭 구멍 갯수, K = 전기용품 사용횟수
N, K = map(int, input().split())

# 전기용품 사용순서대로 입력받음
machines = list(map(int, input().split()))

# 뽑는 횟수
total_cnt = 0

# 멀티탭 꽃혀있는 상황
multitab = [0] * N


# 각 사용에 따라
for i in range(K):
    # 만약 멀티탭 비어있다면 전자기기 꽂기
    for plug in multitab:
        if not plug:
            plug = machines[i]
    # 비어 있는 자리가 없다면
    else:
        # 멀티탭에 있는 애들 중 뒤에 가장 없는 애를 뽑기
        rest_machines = machines[i+1:]
        min_v = float('Inf')
        min_machine = float('Inf')
        for machine in multitab:
            value = rest_machines.count(machine)
            if min_v > value:
                min_v = value
                min_machine = machine
        
        remove_target_idx = multitab.index(min_machine)
        multitab[remove_target_idx] = machines[i]
        total_cnt += 1

print(total_cnt)
    
