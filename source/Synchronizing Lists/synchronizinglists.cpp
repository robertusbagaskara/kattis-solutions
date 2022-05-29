#include <bits/stdc++.h>

using namespace std;

int searchIndex(int arr[], int target, int length) {
    auto itr = find(arr, arr+length, target);
    int index = distance(arr, itr);
    return index;
}

int main() {
    int n=1;
    while (n!=0) {
        cin >> n;
        int arr1[n];
        int arr2[n];
        int tmp[n];
        for (int i=0; i<n; i++) {
            cin >> arr1[i];
        }
        int arr3[n];
        for (int i=0; i<n; i++) {
            arr3[i] = arr1[i];
        }
        for (int i=0; i<n; i++) {
            cin >> arr2[i];
        }
        int n = sizeof(arr1) / sizeof(arr1[0]);
        sort(arr1, arr1 + n);

        for (int i=0; i<n; i++) {
            int index = searchIndex(arr1, arr3[i], n);
            tmp[i] = index;
        }
        sort(arr2, arr2 + n);
        for (int i=0; i<n; i++) {
            cout << arr2[tmp[i]] << "\n";
        }
        cout << "\n";
    }
}
