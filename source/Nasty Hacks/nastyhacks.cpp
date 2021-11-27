#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n, r, e, c;
    cin >> n;
    for (int i=0; i<n; i++) {
        cin >> r >> e >> c;
        if (r+c < e) {
            cout << "advertise" << "\n";
        } else if (r+c > e) {
            cout << "do not advertise" << "\n";
        } else {
            cout << "does not matter" << "\n";
        }
    }

    return 0;
}
