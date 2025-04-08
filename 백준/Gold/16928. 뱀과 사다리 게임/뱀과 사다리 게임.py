import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

ladder = {} # 사다리
snake = {} # 뱀
visited = [0 for _ in range(101)]

for _ in range(N):
    k, v = map(int, input().split())
    ladder[k] = v

for _ in range(M):
    k, v = map(int, input().split())
    snake[k] = v

def check(cur):
    if cur in ladder.keys():
        return ladder[cur]
    if cur in snake.keys():
        return snake[cur]
    return cur
    
def bfs(start):
    q = deque([(start, 0)])
    depth = 0
    
    while q:
        cur, depth = q.popleft()
        depth += 1

        for i in range(1, 7):
            next_ = check(cur + i)
            if visited[next_] or next_ > 100:
                continue
            if next_ == 100:
                return depth
            
            q.append((next_, depth))
            visited[next_] = 1

print(bfs(1))