from collections import deque

N, K = map(int, input().split())
A = deque(list(map(int, input().split())))

robot = deque([0 for _ in range(N)])

# 벨트 회전하기
def move_belt():
    last = A.pop()
    A.appendleft(last)
    robot.pop()
    robot.appendleft(0)
    robot[-1] = 0

level = 0
while True:
    level += 1 # 단계 시작
    # 벨트 이동
    move_belt()
    # 로봇 이동
    for i in range(N-2, -1, -1):
        if robot[i] == 1 and robot[i+1] == 0 and A[i+1] > 0:# 앞에 로봇이 없고 그 칸의 내구도가 1이상
            robot[i] = 0
            robot[i+1] = 1
            A[i+1] -= 1 # 해당 위치 내구도 1 감소
    robot[-1] = 0
    # 로봇 올리기
    if A[0] > 0 and robot[0] == 0:
        A[0] -= 1
        robot[0] = 1
    # K에 도달하면 종료
    if A.count(0) >= K:
        break

print(level)