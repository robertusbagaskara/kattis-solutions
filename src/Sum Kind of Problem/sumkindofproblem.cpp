#include<iostream>
using namespace std;

int positiveSum(int n)
{
    int sum = 0;
    for(int i=0; i<=n; i++){
        sum += i;
    }
    return sum;
}

int oddSum(int n)
{
    int sum = 0;
    for(int i=1; i<=n*2 - 1; i=i+2){
        sum += i;
    }
    return sum;
}

int evenSum(int n)
{
    int sum = 0;
    for(int i=0; i<=n*2; i=i+2){
        sum += i;
    }
    return sum;
}

int main()
{
    int p, k, n, pos, odd, even;
    cin >> p;
    for(int i=0; i<p; i++){
        cin >> k >> n;
        pos = positiveSum(n);
        odd = oddSum(n);
        even = evenSum(n);
        cout << k << " " << pos << " " << odd << " " << even << endl;
    }
}
