import sys
input = sys.stdin.readline

M, N = map(int, input().split())

for num in range(M, N+1):
    if num == 1:
        continue
        
    sqrt = int(num ** 0.5) + 1
    for j in range(2, sqrt):
        if num % j == 0:
            break
    else:
        print(num)