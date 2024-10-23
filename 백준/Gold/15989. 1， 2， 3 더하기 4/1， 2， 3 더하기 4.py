import sys

input = sys.stdin.readline

N = int(input())

dp = [1 for _ in range(10001)] # 모든 수는 1의 합만으로 나타내는 경우의 수 1개씩 있음

# n을 1, 2의 합으로 나타내기 -> n을 1로 나타낸거 + n-2를 1로 나타낸거에 2를 더한거
for i in range(2, 10001): 
    dp[i] += dp[i-2]
# n을 1, 2, 3의 합으로 나타내기 -> n을 1로 나타낸거 + n-3을 1, 2로 나타낸거에 3을 더한거
for i in range(3, 10001):
    dp[i] += dp[i-3]

for _ in range(N):
    n = int(input())
    print(dp[n])