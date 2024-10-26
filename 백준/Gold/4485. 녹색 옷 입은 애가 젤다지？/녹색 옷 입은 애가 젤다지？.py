from heapq import heappush, heappop

problem = 1

while True:
    N = int(input())
    
    if N == 0:
        break
    
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[int(1e9) for _ in range(N)] for _ in range(N)]
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    pq = []
    heappush(pq, (board[0][0], (0, 0))) # 던전 시작 루피, 좌표 입력
    visited[0][0] = board[0][0] # 시작점 0, 0 루피로 갱신
    
    while pq:
        rupee, cur = heappop(pq)
        cur_i, cur_j = cur
        
        if visited[cur_i][cur_j] < rupee: # 더 적은 루피로 방문한적 있으면 continue
            continue
        
        for d in dirs: # 상하좌우 탐색
            ni, nj = cur_i + d[0], cur_j + d[1]
            if 0 <= ni < N and 0 <= nj < N:
                next_val = rupee + board[ni][nj]
                
                if visited[ni][nj] <= next_val: # 더 적은 루피로 방문한적 있으면 continue
                    continue
                visited[ni][nj] = next_val # 지금 값이 최소면 갱신
                heappush(pq, (next_val, (ni, nj)))
    
    print(f'Problem {problem}: {visited[N-1][N-1]}')
    problem += 1