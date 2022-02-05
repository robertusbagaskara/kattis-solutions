#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main() {
    int loop, a, b, c;
    cin >> loop;
    for(int i=0; i<loop; i++){
        cin >> a >> b >> c;
        int arr[] = {a, b, c};
        int n = sizeof(arr)/sizeof(arr[0]);
        sort(arr, arr + n);
        if(arr[0]+arr[1]==arr[2] || arr[0]*arr[1]==arr[2]){
            cout << "Possible" << endl;
        } else {
            cout << "Impossible" << endl;
        }
    }
}
