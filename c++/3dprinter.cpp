#include<iostream>
using namespace std;

int main()
{
    int n, day=1, statue=1;
    cin >> n;
    while(statue<n){
        day++;
        statue *= 2;
    }
    cout << day << endl;
    return 0;
}
