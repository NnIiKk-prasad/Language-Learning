// Printing all binary string of n length
#include <stdio.h>
#include <stdlib.h>
#include <conio.h>

void bin(int n, char A[])
{
    static int count;
    if (n < 1)
    {
        ++count;
        printf("(%d) %s\n", count, A);
    }
    else
    {
        A[n - 1] = '0';
        bin(n - 1, A);
        A[n - 1] = '1';
        bin(n - 1, A);
    }
}

void main()
{
    int n;
    char *c;

    printf("\nEnter a positive integer: ");
    scanf("%d", &n);
    
    c = (char *)malloc((n +1) * sizeof(char));
    c[n] = '\0';

    printf("\nAll binary strings of length %d is:\n", n);
    bin(n, c);
    
    free(c);
    getch();
}
