#include <iostream>

using namespace std;

typedef long long ll;

ll hailstoneRecursive(ll num) {
    if (num==1) return 1;
    if (num%2 == 1) {
        return 1 + hailstoneRecursive(3*num+1);
    } else {
        return 1 + hailstoneRecursive(num/2);
    }
}

int main()
{
    ll n, counter=1;
    cin >> n;
    counter = hailstoneRecursive(n);
    cout << counter << "\n";

    return 0;
}
