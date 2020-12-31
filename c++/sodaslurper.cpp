#include<iostream>
using namespace std;

int main()
{
    int e, f, c, drink = 0, tmp = 0, bottle, mod;
    cin >> e >> f >> c;
    bottle = e + f;
    while (bottle >= c){
        drink = bottle / c;
        tmp += drink;
        mod = bottle % c;
        bottle = drink + mod;
    }
    cout << tmp << endl;
}
