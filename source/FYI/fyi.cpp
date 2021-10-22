#include <iostream>
#include <string.h>
using namespace std;

int main() {
    string n;
    cin >> n;
    if (n.substr(0,3) == "555") {
        cout << 1 << "\n";
    } else {
        cout << 0 << "\n";
    }
    return 0;
}
