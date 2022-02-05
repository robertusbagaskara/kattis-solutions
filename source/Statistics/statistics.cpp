#include <bits/stdc++.h>

using namespace std;

int main()
{
    int flag = 1;
    int N;
    while (cin >> N) {
        int max=-1000000, min=1000000;
        for (int i=0; i<N; i++) {
            int tmp;
            cin >> tmp;
            if (tmp > max) {
                max = tmp;
            }
            if (tmp < min) {
                min = tmp;
            }
        }
        cout << "Case " << flag << ": " << min << " " << max << " " << max-min << "\n";
        flag++;
    }

    return 0;
}
