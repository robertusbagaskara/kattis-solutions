#include <iostream>
using namespace std;

int main(){
    int n, num, l=0;
    cin >> n;
    for(int i=0; i<n; i++) {
        cin >> num;
        l += num;
    }
    cout << l - n + 1 << endl;
    return 0;
}
