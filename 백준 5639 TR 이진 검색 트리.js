const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let data = [];

rl.on('line', (line) => {
    data.push(parseInt(line));
}).on('close', () => {
    postOrder(0, data.length - 1);
    process.exit();
});

function postOrder(start, end) {
    if (start > end) return;

    let div = end + 1;
    for (let i = start + 1; i <= end; i++) {
        if (data[start] < data[i]) {
            div = i;
            break;
        }
    }

    postOrder(start + 1, div - 1);
    postOrder(div, end);
    console.log(data[start]);
}
