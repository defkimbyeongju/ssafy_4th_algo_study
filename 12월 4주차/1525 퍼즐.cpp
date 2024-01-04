#include <iostream>
#include <queue>
#include <unordered_set>
#include <string>
#include <algorithm>
using namespace std;

int bfs(string start) {
    string target = "123456789";
    queue<pair<string, int>> q;
    unordered_set<string> visited;

    q.push(make_pair(start, 0));
    visited.insert(start);

    while (!q.empty()) {
        string current = q.front().first;
        int count = q.front().second;
        q.pop();

        if (current == target) {
            return count;
        }

        int zeroPos = current.find('9');
        int x = zeroPos / 3, y = zeroPos % 3;

        int dx[] = {1, -1, 0, 0}, dy[] = {0, 0, 1, -1};

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i], ny = y + dy[i];
            if (nx >= 0 && nx < 3 && ny >= 0 && ny < 3) {
                string swapped = current;
                swap(swapped[zeroPos], swapped[nx * 3 + ny]);
                if (visited.find(swapped) == visited.end()) {
                    visited.insert(swapped);
                    q.push(make_pair(swapped, count + 1));
                }
            }
        }
    }
    return -1;
}

int main() {
    string board;
    for (int i = 0; i < 9; i++) {
        char num;
        cin >> num;
        board += (num == '0') ? '9' : num;
    }

    int result = bfs(board);
    cout << result << endl;
    return 0;
}
