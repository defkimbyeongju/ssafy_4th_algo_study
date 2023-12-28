#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char state[10];
    int count;
} Node;

typedef struct {
    Node nodes[362880]; // 9! 개의 상태
    int front, rear;
} Queue;

void initQueue(Queue *q) {
    q->front = q->rear = 0;
}

void enqueue(Queue *q, Node node) {
    q->nodes[q->rear++] = node;
}

Node dequeue(Queue *q) {
    return q->nodes[q->front++];
}

int isEmpty(Queue *q) {
    return q->front == q->rear;
}

void swap(char *a, char *b) {
    char temp = *a;
    *a = *b;
    *b = temp;
}

int bfs(char *start) {
    char target[] = "123456789";
    Queue q;
    initQueue(&q);

    Node startNode = {0};
    strcpy(startNode.state, start);
    startNode.count = 0;

    enqueue(&q, startNode);

    while (!isEmpty(&q)) {
        Node current = dequeue(&q);

        if (strcmp(current.state, target) == 0) {
            return current.count;
        }

        int zeroPos;
        for (zeroPos = 0; current.state[zeroPos] != '9'; zeroPos++);

        int x = zeroPos / 3, y = zeroPos % 3;

        int dx[] = {1, -1, 0, 0}, dy[] = {0, 0, 1, -1};

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i], ny = y + dy[i];
            if (nx >= 0 && nx < 3 && ny >= 0 && ny < 3) {
                Node newNode = current;
                int nidx = nx * 3 + ny;
                swap(&newNode.state[zeroPos], &newNode.state[nidx]);
                enqueue(&q, newNode);
            }
        }
    }
    return -1;
}

int main() {
    char board[10] = {0};
    for (int i = 0; i < 9; i++) {
        scanf("%d", &board[i]);
        if (board[i] == 0) board[i] = '9';
        else board[i] += '0';
    }

    int result = bfs(board);
    printf("%d\n", result);
    return 0;
}
