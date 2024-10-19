import sys
from collections import deque

input = sys.stdin.readline

def move(y, x):
    q = deque()
    q.append((y, x))
    union = [(y, x)] # 같은 영역 좌표 모음
    total = populations[y][x]
    while q:
        i, j = q.popleft()
        for dir in dirs:
            ni, nj = i + dir[0], j + dir[1]
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                # 인구 차이가 L 이상 R 이하라면
                if L <= abs(populations[i][j] - populations[ni][nj]) <= R: 
                    # 방문표시, 영역 좌표에 추가, total에 인구수 합산
                    visited[ni][nj] = 1
                    q.append((ni, nj))
                    union.append((ni, nj))
                    total += populations[ni][nj]
    if len(union) <= 1: # 영역이 없으면 0
        return 0
    else: # 있으면 1
        # 인구 재분배하기
        new = total // len(union)
        for uni in union:
            populations[uni[0]][uni[1]] = new
        return 1

N, L, R = map(int, input().split())
populations = [list(map(int, input().split())) for _ in range(N)]
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

ans = 0
while True:
    visited = [[0 for _ in range(N)] for _ in range(N)]
    tmp = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = 1
                tmp += move(i, j)
    # 인구 이동이 있었는지 확인
    if tmp:
        ans += 1
    else:
        break
    
print(ans)