T = int(input())
for tc in range(1,T+1):
    N, K = map(int, input().split())
    q = list(input())
    num_list = []
    div = N // 4
    for _ in range(div): # 4로 나눈 값만큼 회전 반복.
        a = q.pop() 
        q.insert(0,a) # 맨 마지막 문자 빼서 맨 앞으로 보내면 시계 방향 회전임
        for i in range(4): # 매 회전마다 총 4개의 암호가 등장함
            temp = q[div*i:div*(i+1)]
            temp = ''.join(temp)
            num_list.append(int(temp, 16)) # 16진수 정수형으로 변환해서 리스트에 저장

    num_list = list(set(num_list)) # 중복 제거
    num_list.sort(reverse=True) # 내림 차순 정렬
    print(f'#{tc} {num_list[K-1]}') # K번째로 큰 수 출력