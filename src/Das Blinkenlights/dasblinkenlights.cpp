#include <iostream>
using namespace std;

int main() {
    int p, q, s;
    cin >> p >> q >> s;
    bool doubleBlink = false;
    for (int i=1; i<=s; i++) {
        if (i%p == 0 && i%q == 0) {
            doubleBlink = true;
            break;
        }
    }
    if(doubleBlink) {
        cout << "yes" << "\n";
    } else {
        cout << "no" << "\n";
    }
}
