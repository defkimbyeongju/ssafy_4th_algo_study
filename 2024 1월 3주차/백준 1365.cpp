#include <iostream>
#include <vector>
using namespace std;

int binary_search(const vector<int>& sub, int val) {
    int left = 0, right = sub.size() - 1;
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

int min_cut(const vector<int>& connections) {
    vector<int> sub;
    for (int val : connections) {
        int pos = binary_search(sub, val);
        if (pos == sub.size()) {
            sub.push_back(val);
        } else {
            sub[pos] = val;
        }
    }
    return connections.size() - sub.size();
}

int main() {
    int N;
    cin >> N;
    vector<int> connections(N);
    for (int i = 0; i < N; ++i) {
        cin >> connections[i];
    }
    cout << min_cut(connections) << endl;
    return 0;
}