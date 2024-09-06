import sys
input = sys.stdin.readline
        

def move(order): # 주사위 이동별 면 변화 -> 인덱스 0이 윗면, 5가 바닥
    match order:
        case 1:
            dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]
        case 2:
            dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]
        case 3:
            dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]
        case 4:
            dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]


N, M, x, y, K = map(int, input().split())
num_map = [list(map(int, input().split())) for _ in range(N)]
orders = list(map(int, input().split()))

dice = [0, 0, 0, 0, 0, 0] # 주사위: 마주보는 면 인덱스 (0, 5), (1, 4), (2, 3)
cur_x, cur_y = x, y # 주사위 위치
dirs = ((0, 1), (0, -1), (-1, 0), (1, 0)) # 방향: 동서북남

for order in orders:
    next_dir = order-1
    nx, ny = cur_x + dirs[next_dir][0], cur_y + dirs[next_dir][1]
    # print(nx, ny)
    if 0 <= nx < N and 0 <= ny < M: # 다음 방향이 지도 범위일 경우만
        move(order) # 주사위 이동
        if num_map[nx][ny] == 0: # 이동한 칸의 값이 0이면, 주사위 바닥면의 값을 칸에 복사
            num_map[nx][ny] = dice[5]
        else: # 0아니면, 칸에 있는 값이 주사위 바닥면으로 복사 후 칸은 0
            dice[5] = num_map[nx][ny]
            num_map[nx][ny] = 0
        
        print(dice[0]) # 윗면 출력
        cur_x, cur_y = nx, ny