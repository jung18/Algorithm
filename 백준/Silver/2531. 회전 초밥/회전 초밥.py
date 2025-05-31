import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())

nums = []
counter = {}

for _ in range(N):
    num = int(input())
    nums.append(num)
    counter[num] = 0
    
nums = nums + nums

def count(dict, c):
    cnt = 0
    
    for k in dict.keys():
        if dict[k]:
            cnt += 1
    if not dict.get(c, 0):
        cnt += 1
        
    return cnt
    
start, end = 0, k
tmp = nums[start:end]

for num in tmp:
    counter[num] = counter[num] + 1

answer = count(counter, c)

while start < N:
    counter[nums[start]] = counter[nums[start]] - 1
    counter[nums[end]] = counter[nums[end]] + 1
    
    answer = max(answer, count(counter, c))
    
    start += 1
    end += 1
    
print(answer)