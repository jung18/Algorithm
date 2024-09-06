import sys
from collections import deque
input = sys.stdin.readline
        
N = int(input())
K = int(input())
board = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(K):
    i, j = map(int, input().split())
    board[i-1][j-1] = 2 # 보드에 사과 배치
    
L = int(input()) 
change_dir_info = [list(input().split()) for _ in range(L)] # 방향 변환 정보: X초 끝난후, C방향으로 90도 회전
info_sec = [int(row[0]) for row in change_dir_info]
info_dir = [row[1] for row in change_dir_info]

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 우하좌상
snake = deque([(0, 0)]) # 뱀
dir_idx = 0 # 가는 방향
sec = 0 # 경과 시간
i, j = 0, 0 # 뱀 머리

while True:
    sec += 1
    ni, nj = i + dirs[dir_idx][0], j + dirs[dir_idx][1]
    if not (0 <= ni < N and 0 <= nj < N): # 벽에 닿으면 종료
        break
    if (ni, nj) in snake: # 몸에 닿으면 종료
        break
    
    if board[ni][nj] == 2: # 사과 먹으면 늘어남
        snake.append((ni, nj))
        board[ni][nj] = 0
    else: # 사과 없으면 한칸 앞으로
        snake.append((ni, nj))
        snake.popleft()
        
    i, j = ni, nj
    if sec in info_sec:
        change = info_dir[info_sec.index(sec)]
        if change == "D": # 오른쪽 회전
            dir_idx = dir_idx + 1 if dir_idx < 3 else 0
        else: # 왼쪽 회전
            dir_idx = dir_idx - 1 if dir_idx > 0 else 3
print(sec)