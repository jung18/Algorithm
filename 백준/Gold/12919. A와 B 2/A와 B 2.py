import sys

input = sys.stdin.readline

def dfs(pre):
    global ans
    global is_return
    
    if is_return or len(pre) == 0:
        return
    
    if pre == S:
        ans = 1
        is_return = 1
        return
    
    if pre[-1] == 'A': # 마지막이 A면 A없애기
        dfs(pre[:-1])
    if pre[0] == 'B': # 처음이 B면 B없애고 뒤집기
        pre = pre[1:]
        dfs(pre[::-1])
        
S = input().strip()
T = input().strip()
ans = 0
is_return = 0

dfs(T)
print(ans)