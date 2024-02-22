#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_N 20

typedef struct {
    int x, y, dist;
} Position;

typedef struct {
    int front, rear, size;
    Position positions[MAX_N * MAX_N];
} Queue;

void initQueue(Queue *q) {
    q->front = q->rear = q->size = 0;
}

int isEmpty(Queue *q) {
    return q->size == 0;
}

void enqueue(Queue *q, Position pos) {
    q->positions[q->rear] = pos;
    q->rear = (q->rear + 1) % (MAX_N * MAX_N);
    q->size++;
}

Position dequeue(Queue *q) {
    Position pos = q->positions[q->front];
    q->front = (q->front + 1) % (MAX_N * MAX_N);
    q->size--;
    return pos;
}

int board[MAX_N][MAX_N];
int visited[MAX_N][MAX_N];
int N;

int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

typedef struct {
    int x, y, size, eaten;
} Shark;

int compare(const void *a, const void *b) {
    Position *posA = (Position *)a;
    Position *posB = (Position *)b;
    if (posA->dist != posB->dist) return posA->dist - posB->dist;
    if (posA->x != posB->x) return posA->x - posB->x;
    return posA->y - posB->y;
}

Position findFish(Shark shark) {
    Queue q;
    initQueue(&q);
    Position result = {-1, -1, -1};
    memset(visited, 0, sizeof(visited));
    
    enqueue(&q, (Position){shark.x, shark.y, 0});
    visited[shark.x][shark.y] = 1;
    
    Position fishes[MAX_N * MAX_N];
    int fishCount = 0;
    
    while (!isEmpty(&q)) {
        Position pos = dequeue(&q);
        
        for (int i = 0; i < 4; ++i) {
            int nx = pos.x + dx[i], ny = pos.y + dy[i];
            
            if (nx >= 0 && nx < N && ny >= 0 && ny < N && !visited[nx][ny] && board[nx][ny] <= shark.size) {
                visited[nx][ny] = 1;
                enqueue(&q, (Position){nx, ny, pos.dist + 1});
                
                if (board[nx][ny] > 0 && board[nx][ny] < shark.size) {
                    fishes[fishCount++] = (Position){nx, ny, pos.dist + 1};
                }
            }
        }
    }
    
    if (fishCount > 0) {
        qsort(fishes, fishCount, sizeof(Position), compare);
        result = fishes[0];
    }
    
    return result;
}

int main() {
    scanf("%d", &N);
    Shark shark = {0, 0, 2, 0};
    
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            scanf("%d", &board[i][j]);
            if (board[i][j] == 9) {
                shark.x = i;
                shark.y = j;
                board[i][j] = 0;
            }
        }
    }
    
    int time = 0;
    while (1) {
        Position fish = findFish(shark);
        if (fish.x == -1) break;
        
        board[fish.x][fish.y] = 0;
        shark.x = fish.x;
        shark.y = fish.y;
        time += fish.dist;
        shark.eaten++;
        
        if (shark.eaten == shark.size) {
            shark.size++;
            shark.eaten = 0;
        }
    }
    
    printf("%d\n", time);
    return 0;
}
