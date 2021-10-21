#include<stdio.h>

int main()
{
    int N, sum=0;
    scanf("%d", &N);
    int arr[N];
    for (int i=0; i<N; i++) {
        scanf("%d", &arr[i]);
        sum += arr[i];
    }
    printf("%d", sum);

    return 0;
}
