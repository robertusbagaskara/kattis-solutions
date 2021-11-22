#include <bits/stdc++.h>

using namespace std;

int main()
{
    int r, n;
    cin >> r >> n;
    int arr[n];

    for (int i=0; i<n; i++) {
        cin >> arr[i];
    }

    int arrsize = sizeof(arr) / sizeof(arr[0]);
    sort(arr, arr + arrsize);

    for (int i=1; i<=r; i++) {
        int flag = 0;
        for (int j=0; j<n; j++) {
            if (i == arr[j]) {
                flag = 1;
            }
        }

        if (i==r && flag==1) {
            cout << "too late" << "\n";
            break;
        } else if (flag == 0) {
            cout << i << "\n";
            break;
        } else {
            continue;
        }
    }

    return 0;
}
