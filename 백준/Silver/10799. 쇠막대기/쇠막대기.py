import sys
input = sys.stdin.readline

string = input().strip()
stack = [string[0]]

for s in string[1:]: # 레이저 표시
    if stack[-1] == '(' and s == ')':
        stack.pop()
        stack.append('*')
    else:
        stack.append(s)

cnt = 0
answer = 0
for s in stack:
    if s == '(':
        cnt += 1
    elif s == '*':
        answer += cnt
    else:
        answer += 1
        cnt -= 1

print(answer)