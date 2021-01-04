#include<iostream>
using namespace std;

int main()
{
    int N, T, arr[50], sum=0, counter=0;
    cin >> N >> T;
    for(int i=0; i<N; i++) {
        cin >> arr[i];
        if(arr[i] + sum <= T) {
            sum += arr[i];
            counter += 1;
        } else {
            break;
        }
    }
    cout << counter << endl;

    return 0;
}
