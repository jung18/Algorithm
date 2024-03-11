import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())
ground = [[5 for _ in range(N)] for _ in range(N)]  # 처음 땅 (초기 양분은 전부 5)
plus = [list(map(int, input().split())) for _ in range(N)]  # 겨울에 더해질 양분
tree = [[deque() for _ in range(N)] for _ in range(N)]  # 위치별 나무의 나이 정보
for _ in range(M):
    x, y, old = map(int, input().split())
    tree[x-1][y-1].append(old)

for _ in range(K):
    dead = deque()
    # 봄
    for i in range(N):
        for j in range(N):
            len_old = len(tree[i][j])
            for k in range(len_old):  # 각 위치에서 나무 나이정보 순회
                if ground[i][j] >= tree[i][j][k]:  # 나이 이상의 양분이 남아있으면
                    ground[i][j] -= tree[i][j][k]  # 나이만큼 양분 제거
                    tree[i][j][k] += 1  # 나이 1증가
                else:  # 나이보다 적은 양분이 남아있으면
                    for _ in range(k, len_old):  # 이후의 모든 나무는 죽은나무로 분류
                        dead.append((i, j, tree[i][j].pop()))
                    break
    # 여름
    for y, x, old in dead:
        ground[y][x] += (old // 2)  # 죽은 나무 나이//2 만큼 양분 추가

    # 가을
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]
    for i in range(N):
        for j in range(N):
            len_old = len(tree[i][j])
            for k in range(len_old):
                if tree[i][j][k] % 5 == 0:  # 나이가 5의 배수이면
                    for d in dirs:
                        ni, nj = i + d[0], j + d[1]
                        if 0 <= ni < N and 0 <= nj < N:  # 주위 8칸 중 범위 내에 있는 경우만
                            tree[ni][nj].appendleft(1)  # 나이가 1인 나무 추가 (왼쪽에 추가해서 나이순 정렬)
            # 겨울
            ground[i][j] += plus[i][j]  # 양분 추가

ans = 0
for i in range(N):
    for j in range(N):
        ans += len(tree[i][j])
print(ans)