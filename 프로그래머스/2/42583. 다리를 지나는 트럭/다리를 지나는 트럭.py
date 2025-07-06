from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0 for _ in range(bridge_length)])
    trucks = deque(truck_weights)
    answer = 0
    
    tmp = 0
    while bridge:
        tmp -= bridge.popleft()
        
        if trucks:
            if trucks[0] + tmp <= weight:
                t = trucks.popleft()
                bridge.append(t)
                tmp += t
            else:
                bridge.append(0)
        answer += 1
    
    return answer
        
        