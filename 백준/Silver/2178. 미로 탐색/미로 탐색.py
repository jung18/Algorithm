import sys
from collections import deque
input = sys.stdin.readline


def bfs(start):
    q = deque([(start[0], start[1], start[2])])
    answer = 0

    while q:
        i, j, d = q.popleft()
        answer += 1

        if i == N-1 and j == M-1:
            return d

        for dir in dirs:
            ni, nj = i + dir[0], j + dir[1]
            if 0 <= ni < N and 0 <= nj < M:
                if maze[ni][nj] and not visited[ni][nj]:
                    q.append((ni, nj, d+1))
                    visited[ni][nj] = 1


N, M = map(int, input().split())
maze = [[int(m) for m in input().strip()] for _ in range(N)]
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
visited = [[0 for _ in range(M)] for _ in range(N)]

visited[0][0] = 1
print(bfs((0, 0, 1)))