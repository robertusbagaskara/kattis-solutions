#include <bits/stdc++.h>

using namespace std;

int main()
{
    int walkArr[4];

    cin >> walkArr[0] >> walkArr[1] >> walkArr[2] >> walkArr[3];
    int n = sizeof(walkArr) / sizeof(walkArr[0]);
    sort(walkArr, walkArr + n);

    cout << walkArr[0] * walkArr[2] << "\n";

    return 0;
}
