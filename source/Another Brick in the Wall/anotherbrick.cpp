#include<bits/stdc++.h>

using namespace std;

int main()
{
    int h,w,n;
    cin >> h >> w >> n;

    int complete = 0, width=0, height=0;
    for (int i=0; i<n; i++) {
        int brick;
        cin >> brick;
        if (height < h) {
            width += brick;
            if (width == w) {
                height++;
                width = 0;
            } else if (width > w) {
                height = h+1;
            }

            if (height == h) {
                complete = 1;
            }

        }
    }

    if (complete==0) {
        cout << "NO" << "\n";
    } else {
        cout << "YES" << "\n";
    }

    return 0;
}
