#include<iostream>
using namespace std;

int main()
{
    int b, l;

    cin >> b >> l;

    if (b == l) {
        cout << b + l << endl;
    } else if (b > l) {
        cout << l * 2 << endl;
    } else if (b < l) {
        cout << b * 2 << endl;
    }

    return 0;
}
