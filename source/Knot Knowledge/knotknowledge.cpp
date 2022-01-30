#include <bits/stdc++.h>
#include <algorithm>

using namespace std;

int main()
{
    int n;
    cin >> n;
    int x[n], y[n-1];
    for (int i=0; i<n; i++) {
        cin >> x[i];
    }
    for (int i=0; i<n-1; i++) {
        cin >> y[i];
    }

    int xsize = sizeof(x) / sizeof(x[0]);
    int ysize = sizeof(y) / sizeof(y[0]);

    sort(x, x + xsize);
    sort(y, y + ysize);

    int this_num;
    for (int i=0; i<n; i++) {
        int flag = 0;
        for (int j=0; j<n-1; j++) {
            if (x[i] == y[j]) {
                flag = 1;
            }
        }

        if (flag == 0) {
            this_num = x[i];
            break;
        }
    }
    cout << this_num << endl;

    return 0;
}
