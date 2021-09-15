// Pattern Printing 1
#include <stdio.h>

void main()
{
    int i, j, x;
    printf("Enter a number: ");
    scanf("%d", &x);
    for (i = 1; i <= x; i++)
    {
        for (j = 1; j <= i; j++)
        {
            printf("%d ", j);
        }
        printf("\n");
    }
}
