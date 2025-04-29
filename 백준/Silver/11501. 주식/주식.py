import sys
input = sys.stdin.readline

answer = []

for _ in range(int(input())):
    N = int(input())
    nums = list(map(int, input().split()))
    tmp_answer = 0

    tmp_max = nums[-1]
    for i in range(N-1, -1, -1):
        if nums[i] > tmp_max:
            tmp_max = nums[i]
        else:
            tmp_answer += (tmp_max - nums[i])

    answer.append(tmp_answer)

for ans in answer:
    print(ans)