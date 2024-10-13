N = int(input())

info = []
for _ in range(N):
    start, end = map(int, input().split())
    info.append((start, end))

info.sort(key=lambda x: (x[1], x[0])) # 끝나는 시간 순으로 정렬

pre_end = 0
cnt = 0
for start, end in info:
    if start >= pre_end:
        cnt += 1
        pre_end = end
        
print(cnt)