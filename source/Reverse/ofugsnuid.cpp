#include <iostream>
using namespace std;

int main() {
    int i, j, n;
    cin >> n;
    int arr[n];
    for (i=0; i<n; i++) {
        cin >> arr[i];
    }
    for (j=n-1; j>=0; j--) {
        cout << arr[j] << "\n";
    }
    return 0;
}
