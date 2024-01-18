#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};
int n, m;

void dfs(int x, int y, int** field, bool** visited) {
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
    scanf("%d", &t);
    while (t--) {
        int k;
        scanf("%d %d %d", &m, &n, &k);

        int** field = (int**)malloc(n * sizeof(int*));
        bool** visited = (bool**)malloc(n * sizeof(bool*));
        for (int i = 0; i < n; i++) {
            field[i] = (int*)malloc(m * sizeof(int));
            visited[i] = (bool*)malloc(m * sizeof(bool));
            for (int j = 0; j < m; j++) {
                field[i][j] = 0;
                visited[i][j] = false;
            }
        }

        for (int i = 0; i < k; i++) {
            int x, y;
            scanf("%d %d", &y, &x);
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
        printf("%d\n", count);

        for (int i = 0; i < n; i++) {
            free(field[i]);
            free(visited[i]);
        }
        free(field);
        free(visited);
    }
    return 0;
}