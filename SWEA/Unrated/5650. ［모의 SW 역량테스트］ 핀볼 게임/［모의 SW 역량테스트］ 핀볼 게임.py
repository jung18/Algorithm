dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 이동방향: 상, 하, 좌, 우
# 1~5번 튜플: 각 인덱스에 해당하는 블록에 부딫힌 방향에 따른 이동방향 변화 (0번은 사용X)
block = [(), (1, 3, 0, 2), (3, 0, 1, 2), (2, 0, 3, 1), (1, 2, 3, 0), (1, 0, 3, 2)]


def pinball(y, x):
    global max_score

    for d in range(4):
        tmp_score = 0
        i, j = y + dirs[d][0], x + dirs[d][1]

        while True:
            if arr[i][j] == -1 or (i, j) == (y, x):  # 블랙홀 만나거나 시작점으로 돌아오면
                break
            elif 1 <= arr[i][j] <= 5:  # 블록 만나면
                d = block[arr[i][j]][d]  # 해당 블록에 맞게 방향조정
                tmp_score += 1
            elif 6 <= arr[i][j] <= 10:  # 웜홀 만나면
                for k, l, key in wormhole:
                    if (i, j) != (k, l) and arr[i][j] == key:  # 같은 번호의 다른 웜홀로
                        i, j = k, l
                        break
            i, j = i + dirs[d][0], j + dirs[d][1]
        if max_score < tmp_score:
            max_score = tmp_score


for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr = [[5]*(N+2), *[[5]+row+[5] for row in arr], [5]*(N+2)]  # 가장자리에 5번블럭으로 감싸서 벽을 블록과 같이 처리
    wormhole = []  # 웜홀 정보
    max_score = 0

    # 웜홀 위치 찾기
    for i in range(1, N+1):
        for j in range(1, N+1):
            if 6 <= arr[i][j] <= 10:
                wormhole.append((i, j, arr[i][j]))

    # 게임 시작
    for i in range(1, N+1):
        for j in range(1, N+1):
            if arr[i][j] == 0:  # 0인 모든 지점에서 게임 점수 구해보기
                pinball(i, j)

    print(f'#{tc} {max_score}')