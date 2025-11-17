const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const [M, N, K] = input.shift().split(" ").map(Number);

const board = new Array(M).fill().map(() => new Array(N).fill(0));
const visited = new Array(M).fill().map(() => new Array(N).fill(0));

for (let t = 0; t < K; t++) {
    const [x1, y1, x2, y2] = input.shift().split(" ").map(Number); // 왼쪽 아래, 오른쪽 위 좌표

    for (let i = x1; i < x2; i++) {
        for (let j = M-y1-1; j > M-y2-1; j--) {
            board[j][i] = 1;
        }
    }
}

const answer = [];

for (let i = 0; i < M; i++) {
    for (let j = 0; j < N; j++) {
        if (board[i][j] === 0 && visited[i][j] === 0) {
            const queue = [[i, j]];
            let count = 0;
            visited[i][j] = 1
            let head = 0;
            while (head < queue.length) {
                const [ci, cj] = queue[head++];
                count++;
                
                for (const dir of [[0, 1], [0, -1], [1, 0], [-1, 0]]) {
                    const ni = ci + dir[0];
                    const nj = cj + dir[1];

                    if (0 <= ni && ni < M && 0 <= nj && nj < N && visited[ni][nj] === 0 && board[ni][nj] === 0) {
                        queue.push([ni, nj]);
                        visited[ni][nj] = 1;
                    }
                }
            }
            answer.push(count);
        }
    }
}
answer.sort((a, b) => a - b);
console.log(answer.length);
console.log(answer.join(" ").trim());