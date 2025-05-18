import sys
input = sys.stdin.readline

for _ in range(int(input())):
    string = input().strip()
    stack = []
    
    for s in string:
        if not stack or s == '(':
            stack.append(s)
        elif stack[-1] == '(':
            stack.pop()
        else:
            stack.append(s)
    
    if not stack:
        print('YES')
    else:
        print('NO')