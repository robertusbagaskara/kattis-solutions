#include <bits/stdc++.h>
#include <string.h>

using namespace std;

int main()
{
    string symbols;
    int length;

    cin >> symbols;
    length = symbols.length();

    for (int i=0; i<length; i++) {
        if (symbols[i] == ':' || symbols[i] == ';') {
            if (symbols[i+1] == ')') {
                cout << i << endl;
            } else if (symbols[i+1] == '-' && symbols[i+2] == ')') {
                cout << i << endl;
            }
        }
    }

    return 0;
}
