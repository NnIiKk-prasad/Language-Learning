// Program to find sum of 1st 'n' natural numbers and factorial of 'n'
#include <stdio.h>
#include <conio.h>

int sum(int);
int fact(int);

void main()
{
    int s, n;
    unsigned int f;
    printf("Enter a number: ");
    scanf("%d", &n);
    
    s = sum(n);
    printf("\nSum of first %d natural number is %d\n", n, s);
    
    f = fact(n);
    printf("Factorial of %d is %u\n", n, f);
    
    getch();
}

int sum(int n)
{
    int s;
    if (n == 1)
        return (n);
    s = n + sum(n - 1);
    return (s);
}

int fact(int n)
{
    unsigned int f;
    if (n == 1)
        return (n);
    f = n * fact(n - 1);
    return (f);
}
