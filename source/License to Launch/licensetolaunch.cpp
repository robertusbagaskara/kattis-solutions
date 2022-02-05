#include<bits/stdc++.h>

using namespace std;

int main()
{
    int n, day;
    int smallerJunk = 100000;
    cin >> n;
    for (int i=0; i<n; i++) {
        int junk;
        cin >> junk;
        if (junk < smallerJunk) {
            smallerJunk = junk;
            day = i;
        }
    }

    cout << day << endl;
    return 0;
}
