#include<stdio.h>

    int main()
    {
        int a, b, c, d, e, exam;

        scanf("%d %d %d %d %d", &a, &b, &c, &d, &e);
        scanf("%d", &exam);
        if (exam >= a) {
            printf("A\n");
        } else if (exam >= b) {
            printf("B\n");
        } else if (exam >= c) {
            printf("C\n");
        } else if (exam >= d) {
            printf("D\n");
        } else if (exam >= e) {
            printf("E\n");
        } else {
            printf("F\n");
        }

        return 0;
    }
