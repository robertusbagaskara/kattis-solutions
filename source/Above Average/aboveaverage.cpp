#include<iostream>
#include<cstdio>
using namespace std;

int main()
{
    float c, n, grade, sum, total;
    float grades[1000];
    cin >> c;
    for(int i=0; i<c; i++) {
        sum = 0;
        total = 0;
        cin >> n;
        for(int j=0; j<n; j++) {
            cin >> grade;
            sum += grade;
            grades[j] = grade;
        }
        float average = sum / n;
        for(int j=0; j<n; j++) {
            if(grades[j] > average) {
                total++;
            }
        }
        printf("%.3f% \n", (total/n * 100));
    }

    return 0;
}
