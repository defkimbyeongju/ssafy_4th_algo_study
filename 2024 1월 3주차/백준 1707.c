#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct Node {
    int vertex;
    struct Node* next;
} Node;

Node* createNode(int v) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->vertex = v;
    newNode->next = NULL;
    return newNode;
}

void addEdge(Node** graph, int u, int v) {
    Node* newNode = createNode(v);
    newNode->next = graph[u];
    graph[u] = newNode;

    newNode = createNode(u);
    newNode->next = graph[v];
    graph[v] = newNode;
}

bool bfs(Node** graph, int start, int* visited, int V) {
    int* queue = (int*)malloc((V + 1) * sizeof(int));
    int front = 0, rear = 0;
    visited[start] = 1;
    queue[rear++] = start;

    while (front < rear) {
        int node = queue[front++];
        Node* temp = graph[node];
        while (temp) {
            int adjVertex = temp->vertex;
            if (visited[adjVertex] == 0) {
                visited[adjVertex] = -visited[node];
                queue[rear++] = adjVertex;
            } else if (visited[adjVertex] == visited[node]) {
                free(queue);
                return false;
            }
            temp = temp->next;
        }
    }
    free(queue);
    return true;
}

int main() {
    int K;
    scanf("%d", &K);
    for (int k = 0; k < K; k++) {
        int V, E;
        scanf("%d %d", &V, &E);
        Node** graph = (Node**)malloc((V + 1) * sizeof(Node*));
        int* visited = (int*)malloc((V + 1) * sizeof(int));

        for (int i = 1; i <= V; i++) {
            graph[i] = NULL;
            visited[i] = 0;
        }

        for (int i = 0; i < E; i++) {
            int u, v;
            scanf("%d %d", &u, &v);
            addEdge(graph, u, v);
        }

        bool isBipartite = true;
        for (int i = 1; i <= V; i++) {
            if (visited[i] == 0 && !bfs(graph, i, visited, V)) {
                isBipartite = false;
                break;
            }
        }
        printf("%s\n", isBipartite ? "YES" : "NO");

        for (int i = 1; i <= V; i++) {
            Node* temp;
            while (graph[i]) {
                temp = graph[i];
                graph[i] = graph[i]->next;
                free(temp);
            }
        }
        free(graph);
        free(visited);
    }
    return 0;
}