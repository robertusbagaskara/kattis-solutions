#include <iostream>

using namespace std;

int main() {
    long n, w, sum=0;

    cin >> n;
    for (long l=0; l<n; l++) {
        cin >> w;
        sum += w;
    }

    if (sum % 3 == 0) {
        cout << "yes" << endl;
    } else {
        cout << "no" << endl;
    }

    return 0;
}
