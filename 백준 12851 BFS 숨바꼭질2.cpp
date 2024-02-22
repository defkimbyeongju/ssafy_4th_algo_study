#include <iostream>
#include <queue>
#include <vector>
using namespace std;

const int MAX = 100001;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, K;
    cin >> N >> K;

    vector<int> visited(MAX, 0);
    queue<int> queue;
    queue.push(N);
    
    // 경로의 수를 저장할 변수
    int cnt = 0;
    // 결과(최단 거리)
    int result = 0;
    // BFS 실행
    while (!queue.empty()) {
        int curr = queue.front();
        queue.pop();
        
        if (curr == K) {
            if (result == 0) result = visited[curr];
            if (result == visited[curr]) cnt++;
            continue;
        }

        vector<int> next_nums = {curr - 1, curr + 1, curr * 2};
        for (int next_num : next_nums) {
            if (0 <= next_num && next_num < MAX && (visited[next_num] == 0 || visited[next_num] == visited[curr] + 1)) {
                visited[next_num] = visited[curr] + 1;
                queue.push(next_num);
            }
        }
    }

    cout << result << "\n";
    cout << cnt << "\n";

    return 0;
}
