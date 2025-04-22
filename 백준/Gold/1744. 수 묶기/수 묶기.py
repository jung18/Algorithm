import sys
input = sys.stdin.readline

N = int(input())
plus = []
minus = []
answer = 0

for _ in range(N):
    num = int(input().strip())
    if num == 1: # 1반드시 더하기 때문에 미리 더해놓기
        answer += num
    elif num > 0:
        plus.append(num)
    else:
        minus.append(num)

# 양수는 큰거부터, 음수는 작은거부터
plus.sort(reverse=True)
minus.sort()

for i in range(0, len(plus), 2):
    if i < len(plus)-1:
        answer += (plus[i] * plus[i+1])
    else:
        answer += plus[i]

for i in range(0, len(minus), 2):
    if i < len(minus)-1:
        answer += (minus[i] * minus[i+1])
    else:
        answer += minus[i]

print(answer)