#include <bits/stdc++.h>

using namespace std;

int main()
{
    double total=0, C;
    int L;

    cin >> C >> L;
    for (int i=0; i<L; i++) {
        double w, l;
        cin >> w >> l;
        total = total + C*w*l;
    }

    cout << setprecision(10) << total << "\n";

    return 0;
}
