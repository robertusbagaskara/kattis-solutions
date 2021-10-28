#include <bits/stdc++.h>

using namespace std;

int main()
{
    int N, tmp=0, i=1, j=0;
    cin >> N;
    while (tmp < N) {
        tmp += i*i;
        i += 2;
        j += 1;
    }
    if (tmp > N) {
        j -= 1;
    }
    cout << j << endl;

    return 0;
}
