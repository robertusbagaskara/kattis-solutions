#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

/*source: https://en.wikipedia.org/wiki/Bretschneider%27s_formula */
int main()
{
    double s1, s2, s3, s4, semiperimeter;

    cin >> s1 >> s2 >> s3 >> s4;

    semiperimeter = (s1 + s2 + s3 + s4)/2;
    cout << setprecision(7) <<sqrt((semiperimeter - s1) * (semiperimeter - s2) * (semiperimeter - s3) * (semiperimeter - s4)) << endl;

    return 0;
}
