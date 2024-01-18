const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];
let lineNumber = 0;

function bfs(graph, start, visited) {
    let queue = [];
    queue.push(start);
    visited[start] = 1;

    while (queue.length > 0) {
        let node = queue.shift();
        for (let adjNode of graph[node]) {
            if (visited[adjNode] === 0) {
                visited[adjNode] = -visited[node];
                queue.push(adjNode);
            } else if (visited[adjNode] === visited[node]) {
                return false;
            }
        }
    }
    return true;
}

rl.on('line', function (line) {
    input.push(line);
    lineNumber++;
}).on('close', function () {
    let currentLine = 0;
    let testCases = parseInt(input[currentLine++]);
    for (let t = 0; t < testCases; t++) {
        let [V, E] = input[currentLine++].split(' ').map(x => parseInt(x));
        let graph = Array.from({ length: V + 1 }, () => []);
        let visited = new Array(V + 1).fill(0);

        for (let i = 0; i < E; i++) {
            let [u, v] = input[currentLine++].split(' ').map(x => parseInt(x));
            graph[u].push(v);
            graph[v].push(u);
        }

        let isBipartite = true;
        for (let i = 1; i <= V; i++) {
            if (visited[i] === 0 && !bfs(graph, i, visited)) {
                isBipartite = false;
                break;
            }
        }
        console.log(isBipartite ? 'YES' : 'NO');
    }
    process.exit();
});