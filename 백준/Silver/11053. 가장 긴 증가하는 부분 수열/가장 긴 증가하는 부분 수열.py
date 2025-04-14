import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
lis = [arr[0]]


def binary_search(key, start, end):
    while start <= end:
        middle = (start + end) // 2
        if key == lis[middle]:
            return middle
        elif key < lis[middle]:
            end = middle - 1
        else:
            start = middle + 1
    return start 


for i in range(1, N):
    if lis[-1] < arr[i]:
        lis.append(arr[i])
    else:
        lis[binary_search(arr[i], 0, len(lis)-1)] = arr[i]

print(len(lis))
