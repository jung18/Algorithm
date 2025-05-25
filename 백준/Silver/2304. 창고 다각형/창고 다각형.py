import sys

input = sys.stdin.readline

location = []
height = []

N = int(input())

for _ in range(N):
    L, H = map(int, input().split())
    location.append(L)
    height.append(H)

h_list = sorted(height)

# 위치 기준 위치,높이 정렬
for i in range(N-1):
    min_ = i
    for j in range(i+1, N):
        if location[j] < location[min_]:
            min_ = j
    location[i], location[min_] = location[min_], location[i]
    height[i], height[min_] = height[min_], height[i]

start, end, old_h = 0, N-1, 0
answer = 0

# 작은 높이부터 탐색
for h in h_list:
    if h == old_h: # 똑같은 높이는 제외
        continue

    while height[start] < h:
        start += 1
    while height[end] < h:
        end -= 1
    
    answer += ((h - old_h) * (location[end] - location[start] + 1))
    old_h = h

print(answer)