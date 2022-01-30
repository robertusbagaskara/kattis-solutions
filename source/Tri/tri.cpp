#include<iostream>
using namespace std;

void calculate(int a, int b, int c)
{
    if(a + b == c){
        cout << a << "+" << b << "=" << c;
    } else if(a - b == c){
        cout << a << "-" << b << "=" << c;
    } else if(a * b == c){
        cout << a << "*" << b << "=" << c;
    } else if(a / b == c){
        cout << a << "/" << b << "=" << c;
    } else if(a == b + c){
        cout << a << "=" << b << "+" << c;
    } else if(a == b - c){
        cout << a << "=" << b << "-" << c;
    } else if(a == b * c){
        cout << a << "=" << b << "*" << c;
    } else if(a == b / c){
        cout << a << "=" << b << "/" << c;
    }
}

int main()
{
    int a,b,c;
    cin >> a >> b >> c;
    calculate(a, b, c);

    return 0;
}
