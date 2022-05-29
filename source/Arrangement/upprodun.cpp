#include <iostream>

using namespace std;

int main()
{
    int N, M, tmp;
    cin >> N >> M;
    int arr[N];
    tmp = M/N;

    for (int i=0; i<N; i++) {
        arr[i] = tmp;
    }

    if (M%N != 0) {
        for (int i=0; i<(M%N); i++) {
            arr[i] += 1;
        }
    }

    for (int i=0; i<N; i++) {
        for (int j=0; j<arr[i]; j++) {
            cout << "*";
        }
        cout << "\n";
    }

    return 0;
}
