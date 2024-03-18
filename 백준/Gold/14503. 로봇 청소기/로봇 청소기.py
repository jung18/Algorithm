import sys
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())  # d -> 0: 북쪽, 1: 동쪽, 2: 남쪽, 3: 서쪽
arr = [list(map(int, input().split())) for _ in range(N)]  # N x M
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 주변 4칸 방향 (북, 동, 남, 서)
rotation = (3, 0, 1, 2)  # 반시계 방향으로 회전한 경우의 방향
reverse = (2, 3, 0, 1)  # 후진할 경우의 방향
clean = 0  # 청소하는 칸의 개수

i, j = r, c
while True:
    if arr[i][j] == 0:  # 현재 칸이 청소되지 않은 경우
        arr[i][j] = 2  # 현재 칸을 청소
        clean += 1

    for dir in dirs:
        ni, nj = i + dir[0], j + dir[1]
        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:  # 4방향중 청소하지 않은 곳이 있으면
            d = rotation[d]  # 반시계 방향으로 90도 회전
            if arr[i + dirs[d][0]][j + dirs[d][1]] == 0:
                i, j = i + dirs[d][0], j + dirs[d][1]
            break
    else:  # 4방향중 청소되지 않은곳이 없으면
        ni, nj = i + dirs[reverse[d]][0], j + dirs[reverse[d]][1]
        if arr[ni][nj] != 1:  # 후진할 곳이 벽이 아니면
            i, j = ni, nj
        else:  # 벽이라 후진이 불가능하면 정지
            break

print(clean)