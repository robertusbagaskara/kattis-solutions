#include <stdio.h>
int main()
{
    int N;
    scanf("%d", &N);
    if (N % 2 == 0) {
        printf("Bob");
    } else {
        printf("Alice");
    }
    return 0;
}
