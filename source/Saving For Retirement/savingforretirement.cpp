#include<iostream>
using namespace std;

int main()
{
    int B, Br, Bs, A, As, tmp;
    cin >> B >> Br >> Bs >> A >> As;
    tmp = Br - B;
    tmp = tmp * Bs;
    cout << tmp / As + A + 1 << endl;

    return 0;
}
