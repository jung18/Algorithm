def check_line(x, y, cur):
    for i in range(9):
        if i != x and board[y][i] == cur:
            return False
    for i in range(9):
        if i != y and board[i][x] == cur:
            return False
        
    return True

def check_box(x, y, cur): # 박스 검사
    r, c = [], []
    if 0 <= x <= 2:
        c = [0, 1, 2]
    elif 3 <= x <= 5:
        c = [3, 4, 5]
    else:
        c = [6, 7, 8]
        
    if 0 <= y <= 2:
        r = [0, 1, 2]
    elif 3 <= y <= 5:
        r = [3, 4, 5]
    else:
        r = [6, 7, 8]

    for i in r:
        for j in c:
            if x != j and y != i and board[i][j] == cur:
                return False
            
    return True

def dfs(depth, x, y, cur):
    global is_return
    
    if is_return:
        return

    # 문제 있으면 return
    if depth > 0:
        if not check_line(x, y, cur) or not check_box(x, y, cur):
            return
    # 빈간 다채우면 출력
    if depth >= len(zeros):
        for r in board:
            print(''.join(map(str, r)))
        is_return = True
        return
    
    nx, ny = zeros[depth]
    for i in range(1, 10):
        board[ny][nx] = i
        dfs(depth+1, nx, ny, i)
        board[ny][nx] = 0

board = [list(map(int, input())) for _ in range(9)]
zeros = []
is_return = False

for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            zeros.append((j, i))
            
dfs(0, 0, 0, 0)