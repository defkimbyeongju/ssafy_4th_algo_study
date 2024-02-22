const fs = require('fs');
let [n, m, r, ...input] = fs.readFileSync('/dev/stdin').toString().trim().split(/\s+/).map(Number);
const items = input.splice(0, n);
const INF = Number.MAX_SAFE_INTEGER;
const MAX = 101;
const dist = Array.from({ length: MAX }, () => Array(MAX).fill(INF));

for (let i = 1; i <= n; i++) {
    dist[i][i] = 0;
}

for (let i = 0; i < r; i++) {
    const [a, b, l] = [input[i*3], input[i*3+1], input[i*3+2]];
    dist[a][b] = l;
    dist[b][a] = l;
}

function floydWarshall(n, dist) {
    for (let k = 1; k <= n; ++k) {
        for (let i = 1; i <= n; ++i) {
            for (let j = 1; j <= n; ++j) {
                if (dist[i][k] + dist[k][j] < dist[i][j]) {
                    dist[i][j] = dist[i][k] + dist[k][j];
                }
            }
        }
    }
}

floydWarshall(n, dist);

let maxItems = 0;
for (let i = 1; i <= n; ++i) {
    let total = 0;
    for (let j = 1; j <= n; ++j) {
        if (dist[i][j] <= m) {
            total += items[j-1]; // Adjusting index for items array
        }
    }
    maxItems = Math.max(maxItems, total);
}

console.log(maxItems);
