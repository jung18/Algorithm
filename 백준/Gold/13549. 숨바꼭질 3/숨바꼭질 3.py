from collections import deque

N, K = map(int, input().split())

q = deque([N])
visited = [float('inf') for _ in range(100001)]
visited[N] = 0

while q:
    now = q.popleft()
    if now == K:
        print(visited[now])
        break
    
    for next in (now + 1, now - 1, now * 2):
        if 0 <= next <= 100000:
            if next == now * 2 and visited[next] > visited[now]:
                visited[next] = visited[now]
                q.append(next)
            elif visited[next] > visited[now] + 1:
                visited[next] = visited[now] + 1
                q.append(next)