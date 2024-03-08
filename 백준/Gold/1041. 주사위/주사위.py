import sys

N = int(input())
dice = list(map(int, sys.stdin.readline().split()))
min_list = []
ans = 0

if N == 1:
    dice.sort()
    for i in range(5):
        ans += dice[i]

else:
    min_list.append(min(dice[0], dice[5]))
    min_list.append(min(dice[1], dice[4]))
    min_list.append(min(dice[2], dice[3]))
    min_list.sort()

    min1 = min_list[0]
    min2 = min_list[0] + min_list[1]
    min3 = sum(min_list)

    ans1 = ((N-2)**2 + (N-2)*(N-1)*4) * min1
    ans2 = ((N-1)*4 + (N-2)*4) * min2
    ans3 = 4 * min3

    ans = ans1 + ans2 + ans3

print(ans)
