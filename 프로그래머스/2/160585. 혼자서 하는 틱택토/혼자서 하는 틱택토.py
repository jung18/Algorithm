def solution(board):
    cnt_o = 0
    cnt_x = 0
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == "O":
                cnt_o += 1
            elif board[i][j] == "X":
                cnt_x += 1
    
    if cnt_x > cnt_o or cnt_o - cnt_x > 1: # 순서 잘못지킨 경우
        return 0
    
    is_o_win = 0
    is_x_win = 0
    
    def find_winner(line):
        nonlocal is_o_win
        nonlocal is_x_win
        
        if line == "OOO":
            is_o_win = 1
        elif line == "XXX":
            is_x_win = 1
    
    # 가로
    for i in range(3):
        find_winner(board[i])
    
    # 세로
    for i in range(3):
        line = ""
        for j in range(3):
            line += board[j][i]
        find_winner(line)
    
    # 대각선
    line = ""
    for i in range(3):
        line += board[i][i]
    find_winner(line)
    
    line = ""
    for i in range(3):
        line += board[2-i][i]
    find_winner(line)
    
    if is_o_win and is_x_win: # 둘다 이김
        return 0
    if is_o_win and cnt_o == cnt_x: # o가 끝냈는데, x가 둠
        return 0
    if is_x_win and cnt_x < cnt_o: # x가 끝냈는데, o가 둠
        return 0
    
    return 1
        