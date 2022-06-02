#include <bits/stdc++.h>

using namespace std;

int main()
{
    int N, M, total=0;
    cin >> N >> M;

    int visitors = 0;
    for (int i=0; i<M; i++) {
        int group;
        cin >> group;
        if ((N-visitors) >= group) {
            visitors += group;
        } else {
            total += 1;
        }
    }

    cout << total << "\n";

    return 0;
}
