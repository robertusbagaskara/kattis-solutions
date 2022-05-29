#include <iostream>

using namespace std;

int main() {
    int dice[2] = {0,0};
    for (int i=0; i<2; i++) {
        for (int j=0; j<4; j++) {
            int tmp;
            cin >> tmp;
            dice[i] += tmp;
        }
    };

    if (dice[0] > dice[1]) {
        cout << "Gunnar";
    } else if (dice[0] < dice[1]) {
        cout << "Emma";
    } else {
        cout << "Tie";
    }
    return 0;
}
