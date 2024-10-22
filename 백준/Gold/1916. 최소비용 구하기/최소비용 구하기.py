from heapq import heappush, heappop

def djikstra(start):
    pq = []
    heappush(pq, (0, start))
    distance[start] = 0
    while pq:
        w, now = heappop(pq)
        if distance[now] < w:
            continue
        for to_w, to_n in adj[now]:
            new_dis = w + to_w
            if distance[to_n] <= new_dis:
                continue
            distance[to_n] = new_dis
            heappush(pq, (new_dis, to_n))

N = int(input())
M = int(input())

adj = [[] for _ in range(N+1)]
distance = [int(1e9) for _ in range(N+1)]

for _ in range(M):
    start, end, weight = map(int, input().split())
    adj[start].append((weight, end))
start, end = map(int, input().split())

djikstra(start)

print(distance[end])