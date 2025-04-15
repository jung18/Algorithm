import sys
input = sys.stdin.readline

string = input().strip()
target = input().strip()

T = len(target)

stack = []

for s in string:
    stack.append(s)
    if s == target[-1]:
        if len(stack) >= T and ''.join(stack[-T:]) == target:
            del stack[-T:]

answer = ''.join(stack)
print('FRULA' if answer == '' else answer)