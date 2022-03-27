#include <bits/stdc++.h>

using namespace std;

int main() {
    string text, vowels="aiueoAIUEO";
    int counter = 0;
    getline(cin, text);
    for (int i=0; i<text.length(); i++) {
        if (vowels.find(text[i]) != string::npos) {
            counter++;
        }
    }
    cout << counter;
    return 0;
}
