#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n, w, h;
    cin >> n >> w >> h;
    for (int i=0; i<n; i++) {
        int num;
        cin >> num;
        if (num*num <= (w*w) + (h*h)) {
            cout << "DA" << "\n";
        } else {
            cout << "NE" << "\n";
        }
    }

    return 0;
}
