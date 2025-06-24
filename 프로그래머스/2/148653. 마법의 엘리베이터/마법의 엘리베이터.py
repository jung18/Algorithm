def solution(storey):
    answer = 0
    
    while storey:
        # 1의자리 분리
        storey, res = storey // 10, storey % 10
        
        if res < 5 or (res == 5 and storey%10 < 5):
            answer += res      
        else:
            answer += (10-res)
            storey += 1
            
    return answer
        
        
        
        