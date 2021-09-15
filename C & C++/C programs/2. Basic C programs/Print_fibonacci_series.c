// Program to print fibonacci series
#include <stdio.h>

int fib(int n)
{
    int s;
    if (n == 1 || n == 2)
        return (1);
    s = fib(n - 1) + fib(n - 2);
    return (s);
}

void main()
{
    int n, i;
    printf("Enter a number: ");
    scanf("%d", &n);
    printf("First %d terms of fibonacci series are:\n", n);
    for (i = 1; i <= n; i++)
        printf(" %d", fib(i));
}
