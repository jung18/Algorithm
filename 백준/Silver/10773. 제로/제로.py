import sys
input = sys.stdin.readline

answer = []
for _ in range(int(input())):
    num = int(input())

    if num:
        answer.append(num)
    else:
        answer.pop()

print(sum(answer))