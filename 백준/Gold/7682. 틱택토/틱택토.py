def is_triple():
    valid = [(0, 1, 2), (3, 4, 5), (6, 7, 8), 
             (0, 3, 6), (1, 4, 7), (2, 5, 8), 
             (0, 4, 8), (2, 4, 6)]
    x = 0
    o = 0
    
    for val in valid:
        tmp = ''
        for v in val:
            tmp += tik[v]
        if tmp == 'XXX':
            x += 1
        elif tmp == 'OOO':
            o += 1
    return [x, o]

answer = []

while True:
    tik = input()
    if tik == "end":
        break
    
    X_cnt = tik.count('X')
    O_cnt = tik.count('O')
    blank = tik.count('.')
    
    if X_cnt not in (O_cnt, O_cnt+1):
        answer.append('invalid')
        continue
    
    x, o = is_triple()
    if x == 0 and o == 0:
        if blank:
            answer.append('invalid')
        else:
            answer.append('valid')
        continue
    
    if x >= 1 and o >= 1:
        answer.append('invalid')
        continue
    
    if x >= 1:
        if X_cnt > O_cnt:
            answer.append('valid')
        else:
            answer.append('invalid')
    else:
        if X_cnt == O_cnt:
            answer.append('valid')
        else:
            answer.append('invalid')

for ans in answer:
    print(ans)