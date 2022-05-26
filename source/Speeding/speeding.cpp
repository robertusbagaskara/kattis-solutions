#include<iostream>

using namespace std;

int main() {
    int n,t=0,d=0,speed=0;

    cin >> n;
    for (int i=0; i<n; i++) {
        int tmp1, tmp2;
        cin >> tmp1 >> tmp2;
        if (i!=0) {
            if ((tmp2-d)/(tmp1-t) > speed) {
                speed = (tmp2-d) / (tmp1-t);
            }
        }
        t=tmp1;
        d=tmp2;
    }
    cout << speed;
    return 0;
}
