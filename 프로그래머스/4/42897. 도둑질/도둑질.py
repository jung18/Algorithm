def solution(money):
    # 첫 집에서 훔칠 때
    dp1 = [0]*len(money)
    dp1[0] = money[0]

    # 직전 집을 털었을 때와 털지 않았을 때 중에서 더 큰 값 선택해서 갱신
    for i in range(1,len(money)-1): # 첫집 털어서 마지막 집은 제외
        dp1[i] = max(dp1[i-1],money[i] + dp1[i-2])

    # 마지막 집에서 훔칠 때
    dp2 = [0]*len(money)
    dp2[0] = 0 

    for j in range(1,len(money)):
        dp2[j] = max(dp2[j-1],money[j]+dp2[j-2])

    return max(max(dp1),max(dp2))