#include<stdio.h>

int main()
{
    int N;
    scanf("%d", &N);
    for (int i=1; i<=N; i++) {
        char word[100];
        scanf("%s", &word);
        if (i%2 == 1) {
            printf("%s\n", word);
        }
    }
}
