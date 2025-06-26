from collections import deque

def solution(maps):
    N = len(maps[0])
    M = len(maps)

    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    def bfs(start, end):    
        visited = [[0 for _ in range(N)] for _ in range(M)]
        q = deque([start])
        
        while q:
            i, j = q.popleft()
            
            if (i, j) == end:
                return visited[i][j]

            for dir in dirs:
                ni = i + dir[0]
                nj = j + dir[1]

                if 0 <= ni < M and 0 <= nj < N and maps[ni][nj] != "X":
                    if visited[ni][nj]:
                        continue
                    q.append((ni, nj))
                    visited[ni][nj] = visited[i][j] + 1
        
        return -1
                    
    start = [0, 0]
    end = [0, 0]
    lever = [0, 0]
                    
    for i in range(M):
        for j in range(N):
            if maps[i][j] == "S":
                start[0] = i
                start[1] = j
            elif maps[i][j] == "L":
                lever[0] = i
                lever[1] = j
            elif maps[i][j] == "E":
                end[0] = i
                end[1] = j
    
    first = bfs((start[0], start[1]), (lever[0], lever[1]))
    second = bfs((lever[0], lever[1]), (end[0], end[1]))
    
    if first == -1 or second == -1:
        return -1
    else:
        return first + second

    
                

    