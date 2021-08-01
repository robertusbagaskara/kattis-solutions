#include <iostream>
using namespace std;

int main() {
    int tmp = -1, result=1, n, x;
    cin >> n;
    for (int i=0; i<n; i++) {
        cin >> x;
        if (x > tmp && tmp!= -1) {
            result++;
        }
        tmp = x;
    }
    cout << result << endl;
    return 0;
}
