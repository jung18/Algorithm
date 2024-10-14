N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0, 0, 0] for _ in range(N)] for _ in range(N)] # N X N 배열, 현재 칸의 가로, 세로, 대각선 파이프 수

dp[0][1][0] = 1
for i in range(2, N):
    if not board[0][i]:
        dp[0][i][0] = dp[0][i-1][0]

for i in range(1, N):
    for j in range(1, N):
        if board[i][j]: # 현재 칸에 벽있으면 넘어가기
            continue
        # 가로, 세로 파이프 수 갱신
        dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2]
        dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2]
        
        if board[i-1][j] or board[i][j-1]: # 대각선 추가 검사
            continue
        # 대각선 파이프 수 갱신
        dp[i][j][2] = dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2]

print(sum(dp[N-1][N-1]))