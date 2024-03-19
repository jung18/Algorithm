import sys
input = sys.stdin.readline


def push(t):
    global top
    top += 1
    stack[top] = t


N, M = map(int, input().split())
maze = [[c for c in input().strip()] for _ in range(N)]  # 미로
is_visited = [[0 for _ in range(M)] for _ in range(N)]  # 길 표시용 배열
visited = [[0 for _ in range(M)] for _ in range(N)]  # 한번 방문한 좌표 영구기록

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
stack = [(0, 0)] * (M * N)
top = -1
stop = 0

for y in range(N):
    for x in range(M):
        # 시작점 찾으면 탐색 시작
        if (y in (0, N-1) or x in (0, M-1)) and maze[y][x] == '.':
            push((y, x))
            visited[y][x] = 1
            is_visited[y][x] = 1

            while top != -1:
                i, j = stack[top]
                for d in dirs:
                    ni, nj = i + d[0], j + d[1]
                    # 범위 내의 길이면서 방문한 적 없으면
                    if 0 <= ni < N and 0 <= nj < M and maze[ni][nj] == '.' and visited[ni][nj] == 0:
                        # 길 표시
                        is_visited[ni][nj] = 1
                        # 도착점이면 탐색 종료
                        if ni in (0, N - 1) or nj in (0, M - 1):
                            stop = 1
                            break
                        push((ni, nj))
                        # 방문 기록
                        visited[ni][nj] = 1
                        i, j = ni, nj
                        break
                else:  # 주변에 갈 곳 없으면 되돌아가기
                    is_visited[i][j] = 0
                    top -= 1
                if stop:
                    break
        if stop:
            break
    if stop:
        break

# 사용하지 않은 길 @표시
for i in range(N):
    for j in range(M):
        if maze[i][j] == '.' and is_visited[i][j] == 0:
            print('@', end='')
        else:
            print(maze[i][j], end='')
    print()