// -----Arrays in C-----
#include <stdio.h>

int main()
{
    // sum and average of 10 numbers
    int a[10], i, sum = 0;
    float avg;

    printf("Enter 10 numbers\n");
    for (i = 0; i <= 9; i++)
        scanf("%d", &a[i]);

    for (i = 0; i <= 9; i++)
        sum = sum + a[i];

    avg = sum / 10.0;

    printf("\nSum is %d", sum);
    printf("\nAverage is %f", avg);
    // getch();
    return 0;
}
