#include<bits/stdc++.h>

using namespace std;

int main() {
    float l, r;
    cin >> l >> r;
    float c = sqrt(l*l*2);
    if (c < r*2) cout << "fits" << "\n";
    else cout << "nope" << "\n";

    return 0;
}
