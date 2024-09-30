PC = int(input())
N = int(input())


def dfs(idx):
    global cnt 
    
    visited[idx] = 1
    for next_idx in graph[idx]:
        if visited[next_idx]:
            continue
        cnt += 1
        dfs(next_idx)


graph = [[] for _ in range(PC+1)]
visited = [0 for _ in range(PC+1)]
cnt = 0

# 그래프 연결
for _ in range(N):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

visited[1] = 1
dfs(1)
print(cnt)