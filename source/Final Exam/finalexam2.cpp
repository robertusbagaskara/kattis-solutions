#include<iostream>
using namespace std;

int main()
{
    int n;
    int sum = 0;
    cin >> n;
    int arr[n];
    for(int i=0; i<n; i++){
        char ans;
        cin >> ans;
        arr[i] = ans;
    }
    for(int i=0; i<n; i++){
        if(arr[i]==arr[i+1]){
            sum++;
        }
    }
    cout << sum << endl;
}
