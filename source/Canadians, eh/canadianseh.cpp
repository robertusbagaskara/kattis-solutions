#include <bits/stdc++.h>

using namespace std;

int main() {
    string sentence;
    getline(cin, sentence);
    if (sentence.substr(sentence.size() - 3, 3) == "eh?") {
        cout << "Canadian!" << endl;
    } else {
        cout << "Imposter!" << endl;
    }

    return 0;
}
