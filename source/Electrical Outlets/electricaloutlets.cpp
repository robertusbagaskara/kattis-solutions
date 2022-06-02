#include<iostream>
using namespace std;

int main()
{
    int n, k, o, sum;
    cin >> n;
    for(int i=0; i<n; i++) {
        sum = 0;
        cin >> k;
        for(int j=0; j<k; j++) {
            cin >> o;
            sum += o;
        }
        cout << sum - k + 1 << endl;
    }

    return 0;
}
