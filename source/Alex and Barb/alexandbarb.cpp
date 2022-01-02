#include<bits/stdc++.h>

using namespace std;

int main()
{
    long long k, m, n;
    cin >> k >> m >> n;
    if (k%(m+n)<m) {
        cout << "Barb" << "\n";
    } else {
        cout << "Alex" << "\n";
    }

    return 0;
}
