#include <iostream>

using namespace std;

int main() {
    int n, coffee=0, counter=0;
    string s;

    cin >> n;
    cin >> s;

    for (int i=0; i<n; i++) {
        if (s[i] == '1') {
            coffee = 3;
        }
        if (coffee > 0) {
            coffee -= 1;
            counter += 1;
        }
    }

    cout << counter << endl;

    return 0;
}
