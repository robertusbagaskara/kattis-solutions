#include <string>
#include <iostream>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    string sentences;

    cin >> n;

    cin.ignore();
    for(int i=0; i<n; i++) {
        getline(cin, sentences);
        for(int j=0; j<sentences.length(); j++) {
            if(j==0) {
                if (isupper((sentences[j]))){
                        cout << sentences[j];
                } else {
                    cout << (char) toupper(sentences[j]);
                }
            } else {
                cout << (char) tolower(sentences[j]);
            }
        }
        cout << endl;
    }

    return 0;
}
