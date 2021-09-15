// Greatest Common Divisor
#include <stdio.h>

int GCD(int a, int b)
{
    if (a == b)
        return (a);
    if (a % b == 0)
        return (b);
    if (b % a == 0)
        return (a);
    if (a > b)
        return (GCD(a % b, b));
    else
        return (GCD(a, b % a));
}

void main()
{
    int a, b;
    printf("Enter two numbers:\n");
    scanf("%d%d", &a, &b);
    printf("GCD(%d, %d) = %d", a, b, GCD(a, b));
}
