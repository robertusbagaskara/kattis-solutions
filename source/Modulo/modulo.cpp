#include <iostream>
using namespace std;

int main() {
	int arr[10];
	int num, duplicate = 0;
	for(int i=0; i<10; i++) {
		cin >> num;
		arr[i] = num%42;
	}
	for(int i=0; i<10; i++) {
		int temp = 0;
		for(int j =0; j<=i; j++) {
			if(arr[i] == arr[j]) {
				temp += 1;
			}
		}
		if(temp > 1) {
			duplicate += 1;
		}
	}
	cout << 10-duplicate;
}
