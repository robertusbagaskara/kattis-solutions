#include <iostream>

using namespace std;

int main() {
	int loop, num;
	cin >> loop;
	for (int i=0; i<loop; i++) {
		cin >> num;
		if(num%2 == 0) {
			cout << num << " is even \n";
		} else {
			cout << num << " is odd \n";
		}
	}
	return 0;
}
