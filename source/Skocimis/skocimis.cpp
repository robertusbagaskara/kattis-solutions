#include <bits/stdc++.h>

using namespace std;

int main()
{
    int A, B, C;
    cin >> A >> B >> C;
    int moves1 = B-A-1;
    int moves2 = C-B-1;

    if (moves1 > moves2) {
        cout << moves1 << endl;
    } else {
        cout << moves2 << endl;
    }

    return 0;
}

