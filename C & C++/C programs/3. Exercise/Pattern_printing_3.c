// Pattern Printing 3
#include <stdio.h>

void main()
{
    int i, j, x;
    printf("Entr a number: ");
    scanf("%d", &x);
    i = 1;
    while (i <= x)
    {
        j = 1;
        while (j <= i)
        {
            printf("* ");
            j++;
        }
        printf("\n");
        i++;
    }
}
