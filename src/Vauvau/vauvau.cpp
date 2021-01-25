#include<iostream>
using namespace std;

int dog1(int x, int y, int n)
{
    int tmp = 0;
    int ans;
    bool flag = true;
    while(flag) {
        tmp += n;
        if(x >= tmp) {
            flag = false;
            ans = 1;
        } else if (x+y >= tmp) {
            flag = false;
            ans = 0;
        }
    }
    return ans;
}

int dog2(int x, int y, int n)
{
    int tmp = 0;
    int ans;
    bool flag = true;
    while(flag) {
        tmp += x;
        if(tmp >= n) {
            flag = false;
            ans = 1;
        } else if (tmp+y >= n) {
            flag = false;
            ans = 0;
        }
        tmp += y;
    }
    return ans;
}

void calculate(int a, int b, int c, int d, int n)
{
    int ans1, ans2;
    if(a > n) {
        ans1 = dog1(a, b, n);
        ans2 = dog1(c, d, n);
    } else if(a <= n) {
        ans1 = dog2(a, b, n);
        ans2 = dog2(c, d, n);
    }

    if(ans1 == 1 && ans2 == 1){
        cout << "both" << endl;
    } else if(ans1 == 1 || ans2 == 1) {
        cout << "one" << endl;
    } else if(ans1 == 0 && ans2 == 0) {
        cout << "none" << endl;
    }
}


int main()
{
    int a, b, c, d, p, m, g;
    cin >> a >> b >> c >> d;
    cin >> p >> m >> g;
    calculate(a, b, c, d, p);
    calculate(a, b, c, d, m);
    calculate(a, b, c, d, g);

    return 0;
}
