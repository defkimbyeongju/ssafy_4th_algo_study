const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const dx = [1, -1, 0, 0];
const dy = [0, 0, 1, -1];
let n, m, field, visited;

function dfs(x, y) {
    visited[x][y] = true;
    for (let i = 0; i < 4; i++) {
        const nx = x + dx[i];
        const ny = y + dy[i];
        if (nx >= 0 && nx < n && ny >= 0 && ny < m && field[nx][ny] === 1 && !visited[nx][ny]) {
            dfs(nx, ny);
        }
    }
}

let input = [];
rl.on('line', function (line) {
    input.push(line);
}).on('close', function () {
    const t = parseInt(input[0]);
    let currentLine = 1;
    for (let i = 0; i < t; i++) {
        [m, n, k] = input[currentLine++].split(' ').map(Number);
        field = Array.from({ length: n }, () => Array(m).fill(0));
        visited = Array.from({ length: n }, () => Array(m).fill(false));

        for (let j = 0; j < k; j++) {
            const [x, y] = input[currentLine++].split(' ').map(Number);
            field[y][x] = 1; 
        }

        let count = 0;
        for (let y = 0; y < n; y++) {
            for (let x = 0; x < m; x++) {
                if (field[y][x] === 1 && !visited[y][x]) {
                    dfs(y, x);
                    count++;
                }
            }
        }
        console.log(count);
    }
    process.exit();
});