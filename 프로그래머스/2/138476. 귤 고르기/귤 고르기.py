def solution(k, tangerine):
    cnt = [0 for _ in range(max(tangerine)+1)]
    
    for t in tangerine: # 각 귤 수 카운팅
        cnt[t] += 1
    
    cnt.sort(reverse=True)
    
    tmp = 0
    
    for i in range(len(cnt)):
        if tmp + cnt[i] >= k:
            return i+1
        else:
            tmp += cnt[i]
        