import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

# 영역별 인접 노드 수 카운트
def cnt_node(s, area):
    Q = deque([s])
    is_visit = [0 for _ in range(N+1)]
    is_visit[s] = 1
    node_cnt = 1
    while Q:
        node = Q.popleft()
        for next_node in adj_lst[node]:
            if not is_visit[next_node] and next_node in area:
                is_visit[next_node] = 1
                Q.append(next_node)
                node_cnt += 1
    return node_cnt

# 각 영역이 다 이어져 있는지 검사
def validation(select):
    area1 = select
    area2 = [n for n in range(1, N+1) if n not in area1]
    area1_cnt = cnt_node(area1[0], area1)
    area2_cnt = cnt_node(area2[0], area2)
    # 선택된 영역하고 실제 탐색한 연결 영역 크기가 다를경우
    if len(area1) != area1_cnt or len(area2) != area2_cnt:
        return False
    else:
        return True


N = int(input())
population = [0] + list(map(int, input().split()))  # 노드별 인구수
adj_lst = [[]]  # 노드 정보 인접 리스트
for i in range(1, N+1):
    node = list(map(int, input().split()))
    adj_lst.append(node[1:])

min_v = float('inf')

# 각 영역을 선택하는 경우의 수 생성
case = (N-1)//2 + 1 if N % 2 == 0 else (N-1)//2
for i in range(1, case+1):
    my_combi = list(combinations([n for n in range(1, N+1)], i))
    for combi in my_combi:
        if validation(combi):  # 문제없는 경우면
            # 인구수 차 계산
            tmp = abs(sum(population[n] for n in combi)
                      - sum(population[n] for n in [i for i in range(1, N+1) if i not in combi]))
            min_v = min(min_v, tmp)
# 올바르게 구역을 나눌 수 없어서 최소값 변화가 없으면 -1 출력
if min_v == float('inf'):
    min_v = -1
print(min_v)