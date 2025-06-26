def solution(queue1, queue2):
    queue = queue1 + queue2
    target = (sum(queue1) + sum(queue2)) // 2
    
    if (sum(queue1) + sum(queue2)) % 2 == 1:
        return -1
    
    cnt = 0
    start, end = 0, len(queue1)
    q1 = sum(queue1)
    
    while True:
        if start >= end or start >= len(queue) or end >= len(queue):
            return -1
        
        if q1 == target:
            break
        elif q1 > target: # q1 pop
            q1 -= queue[start]
            start += 1
        else: # q2 pop -> q1 insert
            q1 += queue[end]
            end += 1
            
        cnt += 1
    
    return cnt