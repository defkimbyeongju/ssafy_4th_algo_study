#include <iostream>
#include <vector>
#include <queue>
#include <tuple>
#include <algorithm>
using namespace std;

const int dx[4] = {-1, 1, 0, 0};
const int dy[4] = {0, 0, -1, 1};

int main() {
    int N;
    cin >> N;

    vector<vector<int>> board(N, vector<int>(N));
    tuple<int, int, int, int> shark;

    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            cin >> board[i][j];
            if (board[i][j] == 9) {
                shark = make_tuple(i, j, 2, 0);
                board[i][j] = 0;
            }
        }
    }

    auto bfs = [&](tuple<int, int, int, int> shark) -> tuple<int, int, int> {
        vector<vector<bool>> visited(N, vector<bool>(N, false));
        queue<tuple<int, int, int>> q;
        vector<tuple<int, int, int>> fishes;

        int x, y, size, eaten;
        tie(x, y, size, eaten) = shark;
        q.push(make_tuple(x, y, 0));
        visited[x][y] = true;

        while (!q.empty()) {
            int currX, currY, dist;
            tie(currX, currY, dist) = q.front(); q.pop();

            for (int i = 0; i < 4; ++i) {
                int nx = currX + dx[i], ny = currY + dy[i];

                if (nx >= 0 && nx < N && ny >= 0 && ny < N && !visited[nx][ny]) {
                    if (board[nx][ny] > 0 && board[nx][ny] < size) {
                        fishes.emplace_back(dist + 1, nx, ny);
                    }
                    if (board[nx][ny] <= size) {
                        visited[nx][ny] = true;
                        q.push(make_tuple(nx, ny, dist + 1));
                    }
                }
            }
        }

        if (!fishes.empty()) {
            sort(fishes.begin(), fishes.end());
            return fishes[0];
        } else {
            return make_tuple(-1, -1, -1);
        }
    };

    int time = 0;
    while (true) {
        tuple<int, int, int> result = bfs(shark);
        int dist, nx, ny;
        tie(dist, nx, ny) = result;

        if (dist == -1) break;

        board[nx][ny] = 0;
        time += dist;
        get<0>(shark) = nx; get<1>(shark) = ny;
        get<3>(shark)++;

        if (get<2>(shark) == get<3>(shark)) {
            get<2>(shark)++;
            get<3>(shark) = 0;
        }
    }

    cout << time << endl;

    return 0;
}
