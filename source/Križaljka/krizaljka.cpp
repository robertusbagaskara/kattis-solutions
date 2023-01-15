#include <bits/stdc++.h>

using namespace std;

void printLines(int n, int m, int crossedN, int crossedM, string a, string b) {
    for (int j=0; j<m; j++) {
        if (j==crossedM) {
            cout << a;
        } else {
            for (int i=0; i<n; i++) {
                if (i==crossedN) {
                    cout << b[j];
                } else {
                    cout << ".";
                }
            }
        }
        cout << endl;
    }
}

int main() {
    string a, b;
    int n, m, crossedN, crossedM;
    bool flag = false;

    cin >> a;
    cin >> b;
    n = a.length();
    m = b.length();

    for (int i=0; i<n; i++) {
        if (flag) {
            break;
        }
        for (int j=0; j<m; j++) {
            if (a[i] == b[j]) {
                crossedN = i;
                crossedM = j;
                flag = true;
                break;
            }
        }
    }

    printLines(n, m, crossedN, crossedM, a, b);

    return 0;
}
