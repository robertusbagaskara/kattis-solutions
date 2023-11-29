#include <iostream>

using namespace std;

int main() {
    int n, x, a, total=0;

    cin >> n >> x;
    for (int classroom=0; classroom<n; classroom++) {
        cin >> a;
        total += a;
    }

    if (total <= x) {
        cout << "Jebb" << endl;
    } else {
        cout << "Neibb" << endl;
    }

    return 0;
}
