#include<iostream>
using namespace std;

int main()
{
    int A[45];
    int B[45];
    int k;
    A[0] = 0, A[1] = 1, B[0] = 1, B[1] = 1;

    cin >> k;
    if(k>=3) {
        for(int i=2; i<k; i++) {
            A[i] = A[i-1] + A[i-2];
            B[i] = B[i-1] + B[i-2];
        }
    }

    cout << A[k-1] << " " << B[k-1] << endl;

    return 0;
}
