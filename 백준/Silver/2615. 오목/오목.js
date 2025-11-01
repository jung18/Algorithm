const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const board = input.map(line => line.split(" ").map(Number));
let isEnd = false;

function checkWin(i, j) {
    const check = board[i][j];

    for (const dir of [[0, 1], [1, 0], [-1, 1], [1, 1]]) {
        let count = 1;
        let ni = i + dir[0];
        let nj = j + dir[1];

        while (0 <= ni && ni < 19 && 0 <= nj && nj < 19 && board[ni][nj] === check) {
            count++;
            ni += dir[0];
            nj += dir[1];

            if (count === 5) { // 6목인지 확인
                if (0 <= ni && ni < 19 && 0 <= nj && nj < 19 && board[ni][nj] === check) {
                    break;
                } else if (0 <= i-dir[0] && i-dir[0] < 19 && 0 <= j-dir[1] && j-dir[1] < 19 && board[i-dir[0]][j-dir[1]] === check) {
                    break;
                } else {
                    isEnd = true;
                    console.log(check);
                    console.log(i+1, j+1);
                    return;
                }
            }
        }
    }
}

for (let i = 0; i < 19; i++) {
    for (let j = 0; j < 19; j++) {
        if (board[i][j] !== 0) {
            checkWin(i, j);
        }
    }
}

if (!isEnd) {
    console.log(0);
}