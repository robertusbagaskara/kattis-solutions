#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

int main()
{
    int T;
    cin >> T;
    for (int i=0; i<T; i++) {
        ll sum=0, N;
        cin >> N;
        for (ll j=0; j<N; j++) {
            ll candies;
            cin >> candies;
            sum += candies%N;
        }
        if (sum%N == 0) {
            cout << "YES" << "\n";
        } else {
            cout << "NO" << "\n";
        }
    }

    return 0;
}
