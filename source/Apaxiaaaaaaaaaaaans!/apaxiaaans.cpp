#include <iostream>
using namespace std;

int main() {
	string word, nodup;
	cin >> word;
	for(int i=0; i<word.length(); i++) {
		if(i==0) {
			nodup += word[i];
		}
		else {
			if(word[i]!=word[i-1]) {
				nodup += word[i];
			}
		}
	}
	cout << nodup;
	return 0;
}
