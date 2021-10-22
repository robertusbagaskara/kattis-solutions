#include<iostream>
#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t, length, n[99], maxStores, minStores;
    cin >> t;
    for(int i=0; i<t; i++) {
        cin >> length;
        for(int j=0; j<length; j++) {
            cin >> n[j];
        }
        maxStores = n[0];
        minStores = n[0];
        for(int j=0; j<length; j++) {
            if(maxStores < n[j]) {
                maxStores = n[j];
            }
            if(minStores > n[j]) {
                minStores = n[j];
            }
        }
        cout << (maxStores - minStores) * 2 << endl;
    }
    return 0;
}
