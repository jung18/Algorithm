const fs = require("fs");
const [a, k] = fs.readFileSync("/dev/stdin").toString().trim().split(" ").map(Number);

const queue = [a];
const visited = new Map();
visited.set(a, 0);
let head = 0;

while (head < queue.length) { // 꺼낼게 없을 때까지
    const now = queue[head];
    if (now === k) {
        console.log(visited.get(now));
        break;
    }

    for (const next of [now+1, now*2]) {
        if (next <= k && !visited.has(next)) {
            queue.push(next);
            visited.set(next, visited.get(now)+1);
        }
    }
    head++;
}