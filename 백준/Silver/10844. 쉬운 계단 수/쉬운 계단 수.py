import sys
input = sys.stdin.readline

N = int(input())

dp = [[0 for _ in range(N)] for _ in range(10)] # 행: 1~N 자릿수, 열: 0~9 계단수 끝자리 수
answer = 0

for i in range(1, 10): # 1자리 계단수 -> 1~9 다 1개
    dp[i][0] = 1

for i in range(1, N):
    # 끝자리 수가 0, 9 인 i자리 계단수의 개수 => 끝자리가 1, 8이었던 이전 계단수의 개수
    dp[0][i] = dp[1][i-1]
    dp[9][i] = dp[8][i-1]

    # 끝자리 수가 1~8인 i자리 계단수의 개수 => 끝자리가 j에서 +1, -1이었던 이전 계단수의 개수의 합
    for j in range(1, 9):
        dp[j][i] = dp[j-1][i-1] + dp[j+1][i-1]

for i in range(10):
    answer += dp[i][-1]

print(answer % 1000000000)