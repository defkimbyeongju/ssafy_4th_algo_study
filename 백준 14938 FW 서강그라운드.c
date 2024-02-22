#include <stdio.h>
#include <limits.h>

#define INF INT_MAX
#define MAX 101

void floydWarshall(int n, int dist[MAX][MAX]) {
    for (int k = 1; k <= n; ++k) {
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (dist[i][k] != INF && dist[k][j] != INF && dist[i][k] + dist[k][j] < dist[i][j]) {
                    dist[i][j] = dist[i][k] + dist[k][j];
                }
            }
        }
    }
}

int main() {
    int n, m, r;
    scanf("%d %d %d", &n, &m, &r);

    int items[MAX];
    for (int i = 1; i <= n; ++i) {
        scanf("%d", &items[i]);
    }

    int dist[MAX][MAX];
    for (int i = 0; i <= n; ++i) {
        for (int j = 0; j <= n; ++j) {
            if (i == j) dist[i][j] = 0;
            else dist[i][j] = INF;
        }
    }

    for (int i = 0; i < r; ++i) {
        int a, b, l;
        scanf("%d %d %d", &a, &b, &l);
        dist[a][b] = l;
        dist[b][a] = l;
    }

    floydWarshall(n, dist);

    int maxItems = 0;
    for (int i = 1; i <= n; ++i) {
        int total = 0;
        for (int j = 1; j <= n; ++j) {
            if (dist[i][j] <= m) {
                total += items[j];
            }
        }
        if (total > maxItems) {
            maxItems = total;
        }
    }

    printf("%d\n", maxItems);

    return 0;
}
