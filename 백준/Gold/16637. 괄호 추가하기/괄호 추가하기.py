import sys

input = sys.stdin.readline

def cal(a, operator, b):
    a = int(a)
    b = int(b)
    if operator == '*':
        return a * b
    elif operator == '+':
        return a + b
    else:
        return a - b

def dfs(idx, tmp):
    global ans
    
    if idx == N-1:
        if ans < tmp:
            ans = tmp
        return
    # 다음 수가 괄호 X 일 경우 -> 현재값과 다음 수를 연산
    if idx < N-2:
        next_val = cal(tmp, fix[idx+1], fix[idx+2])
        dfs(idx+2, next_val)
    # 다음 수가 괄호 O 일 경우 -> 다음수와 다다음 수를 연산 후 그 값을 현재값과 연산
    if idx < N-4:
        next_val = cal(tmp, fix[idx+1], cal(fix[idx+2], fix[idx+3], fix[idx+4]))
        dfs(idx+4, next_val)
    
N = int(input())
fix = input().strip()
ans = -2 ** 31

dfs(0, int(fix[0]))
print(ans)