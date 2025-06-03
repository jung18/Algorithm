import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
 
def dfs(i):
    for j in range(N):
        if graph[i][j] and not visited[j]:
            visited[j] = 1
            dfs(j)
 
for i in range(N):
    visited = [0 for _ in range(N)]
    dfs(i)
    print(*visited)