const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const N = parseInt(input[0], 10);
const board = input.slice(1, N + 1).map(line => line.split(' ').map(Number));
const dx = [-1, 1, 0, 0];
const dy = [0, 0, -1, 1];
let shark = { x: 0, y: 0, size: 2, eaten: 0 };

for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
        if (board[i][j] === 9) {
            shark.x = i;
            shark.y = j;
            board[i][j] = 0;
            break;
        }
    }
}

function bfs(shark) {
    const visited = Array.from(Array(N), () => Array(N).fill(false));
    const queue = [{ x: shark.x, y: shark.y, dist: 0 }];
    visited[shark.x][shark.y] = true;
    const fishes = [];

    while (queue.length > 0) {
        const { x, y, dist } = queue.shift();

        for (let i = 0; i < 4; i++) {
            const nx = x + dx[i];
            const ny = y + dy[i];

            if (nx >= 0 && nx < N && ny >= 0 && ny < N && !visited[nx][ny]) {
                if (board[nx][ny] <= shark.size) {
                    visited[nx][ny] = true;
                    queue.push({ x: nx, y: ny, dist: dist + 1 });

                    if (board[nx][ny] > 0 && board[nx][ny] < shark.size) {
                        fishes.push({ x: nx, y: ny, dist: dist + 1 });
                    }
                }
            }
        }
    }

    fishes.sort((a, b) => a.dist !== b.dist ? a.dist - b.dist : a.x !== b.x ? a.x - b.x : a.y - b.y);
    return fishes[0];
}

let time = 0;
while (true) {
    const fish = bfs(shark);
    if (!fish) break;

    board[fish.x][fish.y] = 0;
    shark.x = fish.x;
    shark.y = fish.y;
    time += fish.dist;
    shark.eaten++;

    if (shark.eaten === shark.size) {
        shark.size++;
        shark.eaten = 0;
    }
}

console.log(time);
