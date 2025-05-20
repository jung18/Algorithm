import sys
input = sys.stdin.readline

N = int(input())
students = [list(map(int, input().split())) for _ in range(N**2)]
board = [[0 for _ in range(N)] for _ in range(N)] # 교실

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
happy = {
    1:1,
    2:10,
    3:100,
    4:1000
}

for student in students:
    cur = student[0] # 현재 학생
    likes = student[1:] # 좋아하는 학생
    scores = []

    for i in range(N):
        for j in range(N):
            if board[i][j]:
                continue

            tmp_like = 0
            tmp_blank = 0
            for d in dirs:
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < N and 0 <= nj < N:
                    if board[ni][nj] in likes: # 좋아하는 학생 있으면 점수 +1
                        tmp_like += 1
                    if not board[ni][nj]: # 빈칸이면 점수 +1
                        tmp_blank += 1
            scores.append((tmp_like, tmp_blank, i, j))
    
    scores.sort(key=lambda x: (-x[0], -x[1], x[2], x[3])) # 점수는 큰거 우선
    board[scores[0][2]][scores[0][3]] = cur # 학생 배치

students.sort()
answer = 0
for i in range(N):
    for j in range(N):
        cur = board[i][j] # 현재 학생
        tmp_score = 0
        for d in dirs:
            ni, nj = i + d[0], j + d[1]
            if 0 <= ni < N and 0 <= nj < N:
                if board[ni][nj] in students[cur-1][1:]: # 좋아하는 학생 확인
                    tmp_score += 1
        if tmp_score:
            answer += happy[tmp_score]

print(answer)