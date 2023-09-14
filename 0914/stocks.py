T = int(input())
for tc in range(1,T+1):
    ms, ma = map(int, input().split()) # 시드액, 월별 투자 금액
    N, L = map(int, input().split()) # 종목 수, 과거 데이터 입력 기간
    stocks = [list(map(int, input().split())) for _ in range(N)]
    temp = ms # 현재 보유 자산
    for i in range(L):
        profits = []
        for j in range(N):
            if stocks[j][i+1] > stocks[j][i]:
                profits.append([stocks[j][i], stocks[j][i+1], stocks[j][i+1]-stocks[j][i]])
        if profits: # 이익을 내는 종목이 있다면 매수 및 매도 작업 진행
            adds = []
            profits = sorted(profits, key=lambda x: (-x[2], x[0]))
            for k in range(len(profits)):
                buy = temp // profits[k][0] # 현재 가격에서 살 수 있는 만큼만
                temp -= buy*profits[k][0]
                adds.append(buy*profits[k][1])
            temp += sum(adds)
        temp += ma
    print(f'#{tc} {temp-(ms+ma*L)}')