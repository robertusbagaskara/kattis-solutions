#include <bits/stdc++.h>

using namespace std;

int main() {
    string s;
    cin >> s;
    bool flag = false;
    for (int i=0; i<s.length(); i++) {
        if (s[i] == 'a') {
            flag = true;
        }

        if (flag) {
            cout << s[i];
        }
    }
    return 0;
}
