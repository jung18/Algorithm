import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))

prefix_sum = [0 for _ in range(N)]
prefix_sum[0] = A[0]

for i in range(1, N):
    prefix_sum[i] = prefix_sum[i-1] + A[i]

prefix_sum.sort(reverse=True)

print(sum(prefix_sum[:K]))