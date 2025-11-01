const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

let head = 0;
const T = Number(input[head++]);

for (let t = 0; t < T; t++) {
    const [M, N, K] = input[head++].split(" ").map(Number);
    const board = new Array(N).fill().map(() => new Array(M).fill(0));
    const visited = new Array(N).fill().map(() => new Array(M).fill(0));
    let answer = 0;

    for (let k = 0; k < K; k++) {
        const [X, Y] = input[head++].split(" ").map(Number);
        board[Y][X] = 1;
    }

    for (let i = 0; i < N; i++) {
        for (let j = 0; j < M; j++) {
            if (board[i][j] === 1 && visited[i][j] === 0) { // 방문한 적 없는 배추
                // bfs
                const queue = [[i, j]];
                let point = 0;
                visited[i][j] = 1;
                // 상하좌우 탐색
                while (point < queue.length) {
                    const [ci, cj] = queue[point++];
                    for (const dir of [[-1, 0], [0, 1], [1, 0], [0, -1]]) {
                        const ni = ci + dir[0];
                        const nj = cj + dir[1];
                        // 인접한 배추
                        if (0 <= ni && ni < N && 0 <= nj && nj < M && visited[ni][nj] === 0 && board[ni][nj] === 1) {
                            visited[ni][nj] = 1;
                            queue.push([ni, nj]);
                        }
                    }
                }
                answer++;
            }
        }
    }
    console.log(answer);
}