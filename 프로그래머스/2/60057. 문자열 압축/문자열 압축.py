def solution(s):
    N = len(s)
    result = set()
    
    for size in range(1, N+1):
        cnt = 1
        tmp = ''
        string = s[:size]
        for i in range(size, N+size, size):
            if s[i:i+size] == string:
                cnt += 1
            else:
                if cnt > 1:
                    tmp += (str(cnt) + string)
                else:
                    tmp += string
                cnt = 1
                string = s[i:i+size]
        result.add(len(tmp))
        
    return min(result)
                
            