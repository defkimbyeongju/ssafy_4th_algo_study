from itertools import combinations

def chicken_distance(M, city_map):
    house_list = []
    chicken_list = []
    for i in range(N):
        for j in range(N):
            if city_map[i][j] == 1:
                house_list.append((i+1, j+1))
            elif city_map[i][j] == 2:
                chicken_list.append((i+1, j+1))
    # 집과 치킨집의 위치 저장            

    def distance(hr, hc, cr, cc):
        return abs(hr-cr) + abs(hc-cc)
    # 거리 구하는 함수

    min_sum = float('inf')
    
    # 치킨집 중에서 M개를 선택하는 모든 조합
    for selected_chicken in combinations(chicken_list, M):
        sum_cd = 0
        for hr, hc in house_list:
            # 선택된 치킨집 중에서 각 집에 가장 가까운 치킨집 거리를 구하여 더함
            min_cd = min(distance(hr, hc, cr, cc) for cr, cc in selected_chicken)
            sum_cd += min_cd
        # 현재 조합에서의 치킨 거리의 합이 최소인지 확인
        min_sum = min(min_sum, sum_cd)
    return min_sum

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

result = chicken_distance(M, city)
print(result)