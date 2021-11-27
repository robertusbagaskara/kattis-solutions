#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n, t=0;
    cin >> n;
    for (int i=0; i<n; i++) {
        int tmp;
        cin >> tmp;
        if (tmp<0) {
            t++;
        }
    }

    cout << t << "\n";

    return 0;
}
