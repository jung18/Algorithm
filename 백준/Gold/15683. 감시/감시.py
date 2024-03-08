import sys
input = sys.stdin.readline


def combination(i, n):
    if i == n:
        my_combination.append(path.copy())
    else:
        for j in range(4):
            path.append(j)
            combination(i+1, n)
            path.pop()


path = []
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
N, M = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(N)]
my_combination = []
cctv = []
cctv_cnt = 0
for i in range(N):
    for j in range(M):
        if 0 < office[i][j] < 6:
            cctv.append((i, j, office[i][j]))
            if office[i][j] != 5:  # 5번은 돌릴필요가 없음
                cctv_cnt += 1
combination(0, cctv_cnt)

rotation = [(), ((3,), (1,), (2,), (0,)),
            ((2, 3), (0, 1), (2, 3), (0, 1)),
            ((0, 3), (3, 1), (1, 2), (2, 0)),
            ((2, 0, 3), (0, 3, 1), (3, 1, 2), (1, 2, 0))]

min_v = float('inf')

for combi in my_combination:
    idx = 0
    is_view = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if office[i][j] == 6:
                is_view[i][j] = 1

    for i, j, num in cctv:
        if num != 5:
            tmp_rot = rotation[num][combi[idx]]
            idx += 1
        else:
            tmp_rot = (0, 1, 2, 3)

        for d in tmp_rot:
            ni, nj = i, j
            while 0 <= ni < N and 0 <= nj < M and office[ni][nj] != 6:
                is_view[ni][nj] = 1
                ni, nj = ni + dirs[d][0], nj + dirs[d][1]
    min_v = min(min_v, M*N-sum(sum(row) for row in is_view))

print(min_v)