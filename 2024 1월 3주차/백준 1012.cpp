#include <iostream>
#include <vector>
using namespace std;

int dx[] = {1, -1, 0, 0};
int dy[] = {0, 0, 1, -1};
int n, m;

void dfs(int x, int y, vector<vector<int>>& field, vector<vector<bool>>& visited) {
    visited[x][y] = true;
    for (int i = 0; i < 4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];
        if (0 <= nx && nx < n && 0 <= ny && ny < m && field[nx][ny] == 1 && !visited[nx][ny]) {
            dfs(nx, ny, field, visited);
        }
    }
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        int k;
        cin >> m >> n >> k;
        vector<vector<int>> field(n, vector<int>(m, 0));
        vector<vector<bool>> visited(n, vector<bool>(m, false));
        
        for (int i = 0; i < k; i++) {
            int x, y;
            cin >> y >> x;
            field[x][y] = 1;
        }

        int count = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (field[i][j] == 1 && !visited[i][j]) {
                    dfs(i, j, field, visited);
                    count++;
                }
            }
        }
        cout << count << endl;
    }
    return 0;
}