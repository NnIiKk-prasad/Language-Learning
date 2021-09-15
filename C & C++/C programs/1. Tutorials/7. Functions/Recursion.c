// -----Recursion in C-----
#include <stdio.h>

// Sum of first n natural numbers
int firstNsum(int n)
{
    int s = 0;
    if (n == 1)
        return 1;
    s = n + firstNsum(n - 1);
    return s;
}

void main()
{
    int n, s;
    printf("Enter a number: ");
    scanf("%d", &n);
    s = firstNsum(n);
    printf("\nSum of first %d natural numbers is %d", n, s);
}