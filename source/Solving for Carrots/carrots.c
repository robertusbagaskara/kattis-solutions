#include<stdio.h>

int main()
{
    int N;
    int P;
    char describer[100];
    scanf("%d %d", &N, &P);
    for(int i=0; i<N; i++) {
        scanf("%s", &describer);
    }
    printf("%d", P);

    return 0;
}
