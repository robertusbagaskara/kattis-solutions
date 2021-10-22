#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    if (n%4 == 0) {
        cout << "Even" << endl;
    } else if (n%4 == 2) {
        cout << "Odd" << endl;
    } else {
        cout << "Either" << endl;
    }
}
