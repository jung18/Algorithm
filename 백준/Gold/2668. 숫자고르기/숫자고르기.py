import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for i in range(1, N+1):
    node = int(input())
    graph[node].append(i)

answer = []

def dfs(node, path):
    path.append(node)
    visited[node] = 1
    
    for next in graph[node]:
        if next in path: # 사이클
            answer.extend(path)
            return
        else:
            dfs(next, path.copy())

for i in range(1, N+1):
    if not visited[i]:
        dfs(i, [])

answer.sort()
print(len(answer))
for node in answer:
    print(node)