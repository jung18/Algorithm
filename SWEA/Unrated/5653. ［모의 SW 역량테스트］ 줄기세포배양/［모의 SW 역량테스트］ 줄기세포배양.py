dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

for tc in range(1, int(input())+1):
    N, M, K = map(int, input().split())
    cell = [list(map(int, input().split())) for _ in range(N)]
    board = [[[0, 0] for _ in range(380)] for _ in range(380)]
    board_len = len(board)
    cell_point = []  # 줄기세포 좌표 + 생명력

    # board의 중심에 세포 초기 상태정보 만들기
    for i in range(N):
        for j in range(M):
            board[(board_len // 2) - (N // 2) + i][(board_len // 2) - (M // 2) + j][0] = cell[i][j]  # 세포 생명력
            board[(board_len // 2) - (N // 2) + i][(board_len // 2) - (M // 2) + j][1] = cell[i][j]*2  # 살아있는 시간

    # 세포 정보 얻기
    for i in range(board_len):
        for j in range(board_len):
            if board[i][j][0] != 0:
                cell_point.append((i, j, board[i][j][0], board[i][j][1]))
    cell_point.sort(key=lambda x: x[2], reverse=True)  # 생명력 순으로 내림차순 정렬

    # 실험 K번 반복
    for k in range(K):
        tmp_cell = []
        for i, j, X, life in cell_point:
            life -= 1
            if life == X-1:  # 번식
                for d in dirs:
                    ni, nj = i + d[0], j + d[1]
                    if 0 <= ni < board_len and 0 <= nj < board_len:  # board의 범위
                        if board[ni][nj][0] == 0 and board[ni][nj][1] == 0:  # 빈자리면
                            board[ni][nj][0], board[ni][nj][1] = X, X*2  # 번식
                            tmp_cell.append((ni, nj, X, X*2))  # 번식한 세포 정보 추가
            if life == 0:  # 죽은 세포는 버림
                continue
            tmp_cell.append((i, j, X, life))  # 갱신된 세포 정보 추가
        cell_point = tmp_cell

    print(f'#{tc} {len(cell_point)}')