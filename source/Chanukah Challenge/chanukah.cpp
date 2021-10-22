#include <iostream>
using namespace std;

int main() {
	int i, j, loop, index, day, num, sum;
	cin >> loop;
	for(i=0; i<loop; i++) {
		num = 1;
		sum = 0;
		cin >> index >> day;
		for(j=1; j<=day; j++){
			num = num+1;
			sum += num;
		}
		cout << index << " " << sum << endl; 
	}
}
