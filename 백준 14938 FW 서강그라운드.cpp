#include <iostream>
#include <vector>
using namespace std;

const int INF = 1e9; 
const int MAX = 100 + 1; 

void floydWarshall(int n, vector<vector<int>>& dist) {
    for (int k = 1; k <= n; ++k) {
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (dist[i][k] + dist[k][j] < dist[i][j]) {
                    dist[i][j] = dist[i][k] + dist[k][j];
                }
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, r;
    cin >> n >> m >> r;

    vector<int> items(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> items[i];
    }

    vector<vector<int>> dist(MAX, vector<int>(MAX, INF));
    for (int i = 1; i <= n; ++i) {
        dist[i][i] = 0;
    }

    for (int i = 0; i < r; ++i) {
        int a, b, l;
        cin >> a >> b >> l;
        dist[a][b] = l;
        dist[b][a] = l;
    }

    floydWarshall(n, dist);

    int max_items = 0;
    for (int i = 1; i <= n; ++i) {
        int total = 0;
        for (int j = 1; j <= n; ++j) {
            if (dist[i][j] <= m) {
                total += items[j];
            }
        }
        max_items = max(max_items, total);
    }

    cout << max_items << "\n";

    return 0;
}
