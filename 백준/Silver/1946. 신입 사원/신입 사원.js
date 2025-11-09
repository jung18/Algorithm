const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
let head = 0;
const T = Number(input[head++]);

for (let tc = 0; tc < T; tc++) {
    const N = Number(input[head++]);
    const volunteers = new Array(N).fill().map(() => input[head++].split(" ").map(Number));
    let answer = 1;
    
    volunteers.sort((a, b) => a[0] - b[0]); // 서류 기준으로 정렬
    let target = volunteers[0][1]; // 서류 1등의 면접 순위

    for (let i = 1; i < volunteers.length; i++) {
        if (volunteers[i][1] < target) {
            target = volunteers[i][1];
            answer++;
        }
    }

    console.log(answer);
}