#include <bits/stdc++.h>

using namespace std;

int main()
{
    int H, M;
    cin >> H >> M;

    if (H==0 && M>=0 && M<45) {
        cout << H+23 << " " << M+15 << "\n";
    } else if (H==0 && M>=45) {
        cout << H << " " << M-45 << "\n";
    } else if (H<=23 && M>=0 && M<45) {
        cout << H-1 << " " << M+15 << "\n";
    } else if (H<=23 && M>=45) {
        cout << H << " " << M-45 << "\n";
    }

    return 0;
}
