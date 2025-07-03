def solution(people, limit):
    people.sort()
    N = len(people)
    
    if N == 1:
        return 1
    
    start, end = 0, N-1
    
    answer = 0
    while start <= end:        
        if people[start] + people[end] <= limit:
            start += 1
            end -= 1
            answer += 1
        else:
            end -= 1
            answer += 1
        
    return answer