#include <bits/stdc++.h>

using namespace std;

int main()
{
    int N, M;
    cin >> N >> M;

    int visitors = 0;
    for (int i=0; i<M; i++) {
        int group;
        cin >> group;
        visitors += group;
        if (visitors == N) {
            cout << M-(i+1) << endl;
            break;
        } else if (visitors > N) {
            cout << M-i << endl;
            break;
        }
    }

    return 0;
}
