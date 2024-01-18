#include <iostream>
#include <vector>
#include <queue>
using namespace std;

bool bfs(vector<vector<int>>& graph, int start, vector<int>& visited) {
    queue<int> q;
    q.push(start);
    visited[start] = 1;

    while (!q.empty()) {
        int node = q.front();
        q.pop();

        for (int i : graph[node]) {
            if (visited[i] == 0) {
                visited[i] = -visited[node];
                q.push(i);
            } else if (visited[i] == visited[node]) {
                return false;
            }
        }
    }
    return true;
}

int main() {
    int K;
    cin >> K;

    for (int k = 0; k < K; k++) {
        int V, E;
        cin >> V >> E;
        vector<vector<int>> graph(V + 1);
        vector<int> visited(V + 1, 0);

        for (int i = 0; i < E; i++) {
            int u, v;
            cin >> u >> v;
            graph[u].push_back(v);
            graph[v].push_back(u);
        }

        bool is_bipartite = true;
        for (int i = 1; i <= V; i++) {
            if (visited[i] == 0) {
                if (!bfs(graph, i, visited)) {
                    is_bipartite = false;
                    break;
                }
            }
        }

        cout << (is_bipartite ? "YES" : "NO") << endl;
    }
    return 0;
}