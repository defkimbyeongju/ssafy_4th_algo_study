#include <stdio.h>

int binary_search(int sub[], int left, int right, int val) {
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (sub[mid] < val) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return left;
}

int min_cut(int connections[], int N) {
    int sub[N];
    int length = 0;
    for (int i = 0; i < N; i++) {
        int val = connections[i];
        int pos = binary_search(sub, 0, length - 1, val);
        if (pos == length) {
            sub[length++] = val;
        } else {
            sub[pos] = val;
        }
    }
    return N - length;
}

int main() {
    int N;
    scanf("%d", &N);
    int connections[N];
    for (int i = 0; i < N; i++) {
        scanf("%d", &connections[i]);
    }
    printf("%d\n", min_cut(connections, N));
    return 0;
}