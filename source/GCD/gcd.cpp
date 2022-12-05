#include <iostream>

using namespace std;

int main() {
    int a, b, hcf, tmp;
    cin >> a >> b;
    if (a > b) {
        tmp = a;
        a = b;
        b = tmp;
    }
    for (int i=1; i<=a; i++) {
        if (a%i==0 && b%i==0) {
            hcf = i;
        }
    }
    cout << hcf << endl;

    return 0;
}
