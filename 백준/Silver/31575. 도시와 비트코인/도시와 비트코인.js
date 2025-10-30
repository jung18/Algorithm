const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [n, m] = input.shift().split(" ").map(Number);
const board = input.map(line => line.split(" ").map(Number));
const isVisited = new Array(m).fill().map(() => new Array(n).fill(0));
let isReturn = false;

function dfs(i, j) {
    if (i === m-1 && j === n-1) { // 도착
        isReturn = true;
        return;
    }

    for (const dir of [[0, 1], [1, 0]]) {
        const ni = i + dir[0];
        const nj = j + dir[1];
        // 범위 내의 갈수 있는곳 탐색
        if (0 <= ni && ni < m && 0 <= nj && nj < n && 
            board[ni][nj] === 1 && isVisited[ni][nj] === 0 && !isReturn) {
            isVisited[ni][nj] = 1; // 방문표시
            dfs(ni, nj);
        }
    }
}

dfs(0, 0);

if (isReturn) {
    console.log("Yes");
} else {
    console.log("No");
}