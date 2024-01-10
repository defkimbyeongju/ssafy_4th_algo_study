N, K = map(int, input().split())
multitabs = list(map(int, input().split()))
using = []
count = 0
for i in range(K):
    if multitabs[i] in using:
        continue
    if len(using) != N:
        using.append(multitabs[i])
        continue
    # 뽑을 물건의 번호
    pop_plug = 0
    # 멀티탭에 있는 물건 중 가장 나중에 사용될 예정인 물건
    late_use = 0

    for obj in using: # 이후에 쓸 일이 없는 물건들은 다 뽑아버리기
        if obj not in multitabs[i:]:
            pop_plug = obj
            break
        elif multitabs[i:].index(obj) > late_use:
            late_use = multitabs[i:].index(obj)
            pop_plug = obj
    count += 1
    using[using.index(pop_plug)] = multitabs[i]
print(count)


'''
now = []
for i in range(K):
    if multitabs[i] not in now:
        now.append(multitabs[i])
    if len(now) == N:
        break

count = 0
for i in range(K-1):
    if multitabs[i] in now:
        continue
    out_idx = 0 # 기본값 설정
    count += 1
    check = [0]*N
    in_list = []
    for j in range(i+1, K):
        if multitabs[j] in now:
            idx = now.index(multitabs[j])
            in_list.append(idx) # 인덱스로 추가
            check[idx] = 1
    if sum(check) == N:
        now.pop(in_list[-1])
    else:
        now.pop(check.index(0))
    now.append(multitabs[i])

if multitabs[-1] in now:
    print(count)
else:
    print(count+1)
'''