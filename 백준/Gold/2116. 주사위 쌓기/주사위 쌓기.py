N = int(input())
first_dice = list(map(int, input().split()))
# 첫번째 주사위 눈 마주보는 면끼리 묶기
first_grp = [(first_dice[0], first_dice[5]), (first_dice[1], first_dice[3]), (first_dice[2], first_dice[4])]
max_v = 0

# 나머지 주사위 마주보는 면끼리 묶기
dices = [[] for _ in range(N-1)]
for i in range(N-1):
    dice = list(map(int, input().split()))
    dices[i] = [(dice[0], dice[5]), (dice[1], dice[3]), (dice[2], dice[4])]

for case in first_dice:
    eye = case # 첫번째 주사위 윗면
    cases = []
    for j in range(3):
        if eye not in first_grp[j]:
            cases.extend(first_grp[j])
    # 첫번째 주사위 옆면 최대값
    temp_sum = max(cases)

    for dice in dices:
        temp = [] # 한 주사위 옆면 4개
        for j in range(3):
            if eye not in dice[j]:
                temp.extend(dice[j])
            else:
                for k in range(2):
                    if dice[j][k] != eye:
                        eye = dice[j][k] # 아래 주사위 윗면과 같은 면이랑 마주보는 눈으로 변수 값 변경
                        break
        temp_sum += max(temp) # 한 주사위 최대 옆면
    if temp_sum > max_v:
        max_v = temp_sum
print(max_v)