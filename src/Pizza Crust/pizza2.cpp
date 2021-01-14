#include <iostream>
#include <cmath>
#include <iomanip>  //std::setprecission

#define _USE_MATH_DEFINES

using namespace std;

int main() {
	int r, c;
	float totalArea, cheeseArea;
	cin >> r >> c;
	totalArea = M_PI*r*r;
	cheeseArea = M_PI*(r-c)*(r-c);
	std::cout << std::setprecision(8) << (cheeseArea/totalArea*100) << endl;
	return 0;
}
