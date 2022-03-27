#include <bits/stdc++.h>

using namespace std;

int main() {
    int g, t, n, items=0, weight;
    cin >> g >> t >> n;
    weight = g - t;
    for (int i=0; i<n; i++) {
        int tmp;
        cin >> tmp;
        items += tmp;
    }

    cout << (0.9*weight) - items << "\n";

    return 0;
}
