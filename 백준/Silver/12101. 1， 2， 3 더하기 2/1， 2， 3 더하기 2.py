def dfs(depth):
    global cnt
    global stop
    
    if stop: # k번째 찾았으면 종료
        return
    
    if len(arr) > n: # 1을 n개 까지만 뽑도록
        return
    
    if sum(arr) > n: # 뽑은 수 합이 이미 n을 넘었으면 종료
        return
    
    if sum(arr) == n: # 뽑은 수 합이 n이면 카운트
        cnt += 1
    
    if cnt == k: # k번째 찾았으면 종료하도록 stop -> True
        print("+".join(map(str, arr)))
        stop = True
        return
        
    for i in range(1, 4):
        arr.append(i)
        dfs(depth+1)
        arr.pop()


n, k = map(int, input().split())
cnt = 0
arr = []
stop = False
dfs(1)

if not stop: # 함수 종료 후에도 k번째가 없었으면 -1 출력
    print(-1)