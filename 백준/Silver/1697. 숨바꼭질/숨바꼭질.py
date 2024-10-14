from collections import deque

N, K = map(int, input().split())
q = deque([N])
visited = [0 for _ in range(100001)]

while q:
    x = q.popleft()
    if x == K: # 잡았는지 확인
        print(visited[x])
        break
    # 못잡았으면 3가지 경우의 수 추가
    for next in (x-1, x+1, x*2):
        # 범위 안에서만
        if 0 <= next <= 100000 and not visited[next]:
            visited[next] = visited[x] + 1
            q.append(next)