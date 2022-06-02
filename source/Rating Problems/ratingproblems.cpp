#include <cstdio>

int main() {
    int k, total;
    float n, minimum, maximum;
    scanf("%f %d", &n, &k);
    total = 0;
    for (int i=0; i<k; i++) {
        int r;
        scanf("%d", &r);
        total += r;
    }
    minimum = (total + (n-k)*-3) / n;
    maximum = (total + (n-k)*3) / n;
    printf("%f %f", minimum, maximum);
    return 0;
}
