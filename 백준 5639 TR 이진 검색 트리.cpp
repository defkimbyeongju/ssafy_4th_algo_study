#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 10000

int data[MAX_SIZE];
int count = 0;

void postOrder(int start, int end) {
    if (start > end) return;

    int div = end + 1;
    for (int i = start + 1; i <= end; ++i) {
        if (data[start] < data[i]) {
            div = i;
            break;
        }
    }

    postOrder(start + 1, div - 1);
    postOrder(div, end);
    printf("%d\n", data[start]);
}

int main() {
    while (scanf("%d", &data[count]) != EOF) {
        count++;
    }

    postOrder(0, count - 1);
    return 0;
}
