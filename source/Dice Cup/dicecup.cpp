#include<iostream>
using namespace std;
int large, small;

void choose(int x, int y)
{
    if(x>y){
        large = x;
        small = y;
    } else {
        large = y;
        small = x;
    }
}

int main()
{
    int x,y;
    cin >> x >> y;
    choose(x,y);
    for(int i = small+1; i<=large+1; i++){
        cout << i << endl;
    }
    return 0;
}
