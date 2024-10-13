name = sorted(input()) # 사전순 정렬

tmp = name[0]
cnt = 1
cnt_char = []

# 알파벳 개수 세기
for i in range(1, len(name)):
    if name[i] == tmp:
        cnt += 1
    else:
        cnt_char.append((tmp, cnt))
        tmp = name[i]
        cnt = 1
else:
    cnt_char.append((tmp, cnt))

odd_cnt = 0
middle = ''
palindrome = ''
for char, num in cnt_char: 
    if num % 2 == 1:
        odd_cnt += 1
        middle = char # 가운데 들어갈 문자
    if odd_cnt >= 2: # 홀수 알파벳이 2개이상 있으면 팰린드롬 불가능
        print("I'm Sorry Hansoo")
        break
    palindrome += (char * (num//2))
else:
    print(palindrome + middle + palindrome[::-1])