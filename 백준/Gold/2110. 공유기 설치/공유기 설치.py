import sys
input = sys.stdin.readline

N, C = map(int, input().split())
home = [int(input().strip()) for _ in range(N)]
home.sort()

answer = 0

# 거리 최대, 최소
start = 1
end = home[-1] - home[0]

# 적절한 거리값 찾기
while start <= end:
    middle = (start + end) // 2
    cnt = 1
    current = home[0]

    # 임의의 거리(middle)에서의 공유기 갯수 카운팅
    for i in range(1, len(home)):
        if home[i] >= current + middle:
            current = home[i]
            cnt += 1

    if cnt >= C: # 갯수가 많으면 거리 늘리기 -> C개가 되는 middle을 찾아도 최대 거리 확인을 위해 종료 X
        answer = middle
        start = middle + 1
    else: # 갯수가 적으면 거리 줄이기
        end = middle - 1

print(answer)