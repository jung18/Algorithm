import sys
from itertools import permutations
input = sys.stdin.readline

# 각 결과에 따라 이닝 점수 계산
def baseball(per, play):
    global per_idx
    b1, b2, b3 = 0, 0, 0
    result = 0
    out = 0
    while out < 3:
        s = play[per[per_idx]]
        if s == 1:
            result += b3
            b1, b2, b3 = 1, b1, b2
        elif s == 2:
            result += (b2 + b3)
            b1, b2, b3 = 0, 1, b1
        elif s == 3:
            result += (b1 + b2 + b3)
            b1, b2, b3 = 0, 0, 1
        elif s == 4:
            result += (b1 + b2 + b3 + 1)
            b1, b2, b3 = 0, 0, 0
        else:
            out += 1
        per_idx = 0 if per_idx == 8 else per_idx + 1

    return result


N = int(input())
players = [list(map(int, input().split())) for _ in range(N)]
max_score = 0

for per in permutations([i for i in range(1, 9)]):  # 타순 정하기
    per = list(per)
    per.insert(3, 0)  # 1번 타자를 4번째로 배치
    per_idx = 0
    tmp = 0
    for play in players:  # 각 이닝
        tmp += baseball(per, play)
    max_score = max(max_score, tmp)

print(max_score)