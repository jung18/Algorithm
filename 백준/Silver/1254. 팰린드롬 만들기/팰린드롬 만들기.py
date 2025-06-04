import sys
input = sys.stdin.readline

S = input().strip()

for i in range(len(S)):
    if S[i:] == S[i:][::-1]: # 특정 구간이 팰린드롬
        print(len(S) + i) 
        break