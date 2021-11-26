#include <iostream>

using namespace std;

int main()
{
    int X,Y;
    cin >> X >> Y;
    if (Y % 2 == 1) {
        cout << "impossible" << "\n";
    } else {
        cout << "possible" << "\n";
    }

    return 0;
}
