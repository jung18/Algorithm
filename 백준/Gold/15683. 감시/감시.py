import sys
input = sys.stdin.readline

# 1~4 번 cctv의 각 방향을 정할 조합 생성
def combination(i, n):
    if i == n:
        my_combination.append(path.copy())
    else:
        for j in range(4):
            path.append(j)
            combination(i+1, n)
            path.pop()


path = []
N, M = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(N)]
my_combination = []
cctv = []  # cctv위치와 번호 저장
cctv_cnt = 0  # 5번 제외 나머지 cctv수
for i in range(N):
    for j in range(M):
        if 0 < office[i][j] < 6:
            cctv.append((i, j, office[i][j]))
            if office[i][j] != 5:  # 5번은 회전시킬 필요가 없으니 제외
                cctv_cnt += 1
combination(0, cctv_cnt)

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 방향벡터

# cctv 종류별로 회전할 때 바라볼 방향벡터 지정
# 1~4번 인덱스를 cctv번호로 사용, 0번 인덱스는 사용 X
rotation = [(), ((3,), (1,), (2,), (0,)),
            ((2, 3), (0, 1), (2, 3), (0, 1)),
            ((0, 3), (3, 1), (1, 2), (2, 0)),
            ((2, 0, 3), (0, 3, 1), (3, 1, 2), (1, 2, 0))]

min_v = float('inf')
# 각 방향 조합에 대해 사각지대 확인
for combi in my_combination:
    idx = 0
    is_view = [[0 for _ in range(M)] for _ in range(N)]  # 볼수 있는 지점 표시용 배열
    # 벽 위치 표시
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
        # 배열 범위 내에서 벽을 만날 때 까지 해당 방향으로 계속 진행
        for d in tmp_rot:
            ni, nj = i, j
            while 0 <= ni < N and 0 <= nj < M and office[ni][nj] != 6:
                is_view[ni][nj] = 1
                ni, nj = ni + dirs[d][0], nj + dirs[d][1]
    min_v = min(min_v, M*N-sum(sum(row) for row in is_view))

print(min_v)