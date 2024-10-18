for _ in range(3):
    total = 0 
    coins = [] 
    N = int(input())
    for _ in range(N):
        coin, n = map(int, input().split())
        coins.append((coin, n))
        total += coin * n
    
    if total % 2 != 0: # 전체 금액이 홀수면 절대 반띵 불가능
        print(0)
        continue

    total //= 2
    
    # 절반 금액을 채울 수 있는지 동전 하나씩 확인
    dp = [True] + [False] * total
    for coin, n in coins:
        for i in range(total, coin-1, -1):
            if dp[i-coin]:
                for j in range(n):
                    next = i + coin * j
                    if next <= total:
                        dp[next] = True
                    else:
                        break
        if dp[-1]: # 절반 금액을 채웠으면 1
            print(1)
            break
    else: # 아니면 0
        print(0)