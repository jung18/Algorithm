const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const N = Number(input.shift());
const nodes = input.map(line => line.split(" ").map(Number));

const graph = new Array(N+1).fill().map(() => []);
const parents = new Array(N+1).fill(0);

for (const [n1, n2] of nodes) {
    // 방향 없는 그래프
    graph[n1].push(n2);
    graph[n2].push(n1);
}

let head = 0;
const queue = [1];

while (head < queue.length) {
    const now = queue[head++];
    for (const child of graph[now]) {
        if (parents[child] === 0 && child !== 1) { // 1번 노드 제외
            parents[child] = now;
            queue.push(child);
        }
    }
}

for (let i = 2; i < parents.length; i++) {
    console.log(parents[i]);
}