import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

cnt = [0] * (max(arr) + 1) # arr의 각 원소 카운팅
left, right = 0, 0 # 투 포인터
answer = 0 

while right < N:
    if cnt[arr[right]] < K: # 중복 K개 이하면 전진
        cnt[arr[right]] += 1
        right += 1
    else: # 중복 K 개 초과면 하나 빼기
        cnt[arr[left]] -= 1
        left += 1
    answer = max(answer, right - left)
    
print(answer)