// Pattern Printing 2
#include <stdio.h>

void main()
{
    int i, j, k, x;
    printf("Enter a number: ");
    scanf("%d", &x);
    for (i = x; i >= 1; i--)
    {
        for (j = i; j < x; j++)
        {
            printf("  ");
        }
        for (k = 1; k <= i; k++)
        {
            printf("%d ", k);
        }

        printf("\n");
    }
}
