import sys
input = sys.stdin.readline

N = int(input())
rank = sorted([int(input()) for _ in range(N)])

ans = 0
for i in range(1, N+1):
    if i != rank[i-1]:
        ans += abs(rank[i-1]-i)

print(ans)