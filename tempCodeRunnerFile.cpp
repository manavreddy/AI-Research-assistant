#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>
using namespace std;

int min_travel_time(int m, int n, vector<int>& transitionTime, vector<int>& requestedHubs) {
    int current = requestedHubs[0];
    int total_time = 0;

    int total_ring_time = 0;
    for (int i = 1; i <= m; i++)
        total_ring_time += transitionTime[i];

    for (int i = 1; i < n; i++) {
        int target = requestedHubs[i];

        if (current == target) continue;

        // Clockwise: current -> target
        int clockwise_time = 0;
        int pos = current;
        while (pos != target) {
            clockwise_time += transitionTime[pos];
            pos = (pos % m) + 1;
        }

        // Counterclockwise = total - clockwise
        int counterclockwise_time = total_ring_time - clockwise_time;

        total_time += min(clockwise_time, counterclockwise_time);
        current = target;
    }

    return total_time;
}

int main() {
    int m = 3;
    int n = 4;

    // 1-indexed: transitionTime[1]=3, [2]=2, [3]=1
    vector<int> transitionTime = {0, 3, 2, 1};
    vector<int> requestedHubs  = {1, 3, 3, 2};

    int result = min_travel_time(m, n, transitionTime, requestedHubs);
    cout << "Total minimum time: " << result << endl;  // Expected: 4

    return 0;
}