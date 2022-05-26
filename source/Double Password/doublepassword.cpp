#include<bits/stdc++.h>

using namespace std;

int main() {
    int counter=0;
    string password1, password2;
    cin >> password1 >> password2;
    for (int i=0; i<password1.length(); i++) {
        if (password1[i] != password2[i]) {
            counter++;
        }
    }
    cout << pow(2, counter) << "\n";

    return 0;
}
