import sys
from itertools import combinations
input = sys.stdin.readline

# 도시의 치킨거리 구하기
def chicken_distance(chicken_lst):
    min_sum = 0 # 도시의 치킨 거리
    for i in range(N):
        for j in range(N):
            if city[i][j] == 1:
                tmp_min = 2 * N  # 각 집의 치킨 거리
                for k, l in chicken_lst:
                    tmp_min = min(tmp_min, (abs(i-k) + abs(j-l)))
                min_sum += tmp_min
    return min_sum


N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]  # 0: 빈칸, 1: 집, 2: 치킨집
chicken = [(i, j) for i in range(N) for j in range(N) if city[i][j] == 2]  # 치킨집 위치들
my_combination = combinations(chicken, M)  # 전체 치킨집중 M개 뽑는 조합
min_v = float('inf')

for combi in my_combination:
    min_v = min(min_v, chicken_distance(combi))

print(min_v)