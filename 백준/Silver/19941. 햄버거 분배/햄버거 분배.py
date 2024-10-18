import sys

input = sys.stdin.readline

N, K = map(int, input().split())
ph = list(input())

cnt = 0
visited = [0 for _ in range(N)]
for i in range(N):
    if ph[i] == 'P':
        for j in range(i-K, i+K+1):
            # 먼 햄버거부터 찾아서 먹기 왼 -> 오
            if 0 <= j < N and ph[j] == 'H' and not visited[j]:
                visited[j] = 1
                cnt += 1
                break
print(cnt)