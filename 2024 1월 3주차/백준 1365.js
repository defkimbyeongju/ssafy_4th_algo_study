const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

const N = parseInt(input[0]);
const connections = input[1].split(' ').map(Number);

function binarySearch(sub, val) {
    let left = 0, right = sub.length - 1;
    while (left <= right) {
        let mid = Math.floor((left + right) / 2);
        if (sub[mid] < val) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return left;
}

function minCut(connections) {
    let sub = [];
    for (let val of connections) {
        let pos = binarySearch(sub, val);
        if (pos === sub.length) {
            sub.push(val);
        } else {
            sub[pos] = val;
        }
    }
    return connections.length - sub.length;
}

console.log(minCut(connections));