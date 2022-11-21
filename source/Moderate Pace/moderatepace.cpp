#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    cin >> n;
    int distance[3][n];

    for (int i=0; i<3; i++) {
        for (int j=0; j<n; j++) {
            int num;
            cin >> num;
            distance[i][j] = num;
        }
    }

    for (int i=0; i<n; i++) {
        int temp[] = {distance[0][i], distance[1][i], distance[2][i]};
        int sizeTemp = sizeof(temp) / sizeof(temp[0]);
        sort(temp, temp + sizeTemp);
        cout << temp[1] << " ";
    }

    return 0;
}
