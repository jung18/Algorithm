import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
trues = list(map(int, input().split()))[1:]  # 진실 아는 사람 번호
parties = []
is_visited = [0] * M  # 각 파티 체크용 배열
for _ in range(M):
    parties.append(list(map(int, input().split()))[1:])
Q = deque(trues)

while Q:
    cur = Q.popleft()  # 진실 아는 사람 번호 하나씩 꺼내기
    for i in range(M):
        if cur in parties[i] and is_visited[i] == 0:  # 확인 안한 파티에 진실 아는사람이 있으면
            is_visited[i] = 1  # 확인 표시
            for p in parties[i]:  # 그 파티의 나머지 번호들 추가
                if cur != p:
                    Q.append(p)
print(M-sum(is_visited))
