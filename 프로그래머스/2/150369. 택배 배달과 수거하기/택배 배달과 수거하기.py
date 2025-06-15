def solution(cap, n, deliveries, pickups):
    deliveries = [(i+1, deliveries[i]) for i in range(n) if deliveries[i]]
    pickups = [(i+1, pickups[i]) for i in range(n) if pickups[i]]
    answer = 0
    
    def f(home):
        max_dis = 0
        tmp = 0
        while home:
            dis, box = home.pop()
            max_dis = max(dis, max_dis)

            if tmp + box > cap: # 다 못담으면 남겨놓기
                home.append((dis, (tmp+box) - cap))
                break
            else:
                tmp += box
        return max_dis
    
    while deliveries or pickups:
        answer += max(f(deliveries), f(pickups)) * 2 # 배달, 픽업 중 더 먼거리 기준
    
    return answer
        