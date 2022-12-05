#include <iostream>

using namespace std;

int main() {
    int R, C, Zr, Zc;
    string s;
    cin >> R >> C >> Zr >> Zc;
    for (int i=0; i<R; i++) {
        cin >> s;
        for (int j=0; j<Zr; j++) {
            for (int k=0; k<C; k++) {
                for (int l=0; l<Zc; l++) {
                    cout << s[k];
                }
            }
            cout << "\n";
        }
    }
    return 0;
}
