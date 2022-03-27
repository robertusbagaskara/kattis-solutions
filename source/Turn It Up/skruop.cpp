#include<bits/stdc++.h>

using namespace std;

int main() {
    int n, volume=7;
    cin >> n;
    for (int i=0; i<=n; i++) {
        string request;
        getline(cin, request);
        if (request=="Skru op!" && volume<10) {
            volume++;
        } else if (request=="Skru ned!" && volume>0) {
            volume--;
        }
    }
    cout << volume << "\n";

    return 0;
}
