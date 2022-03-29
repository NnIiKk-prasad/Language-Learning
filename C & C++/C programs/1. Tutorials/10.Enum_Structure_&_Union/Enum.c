// -----Enum in C-----
#include <stdio.h>

enum boolean
{
    false,
    true
};

enum boolean isEven(int x)
{
    if (x % 2 == 0)
        return true;
    else
        return false;
}

void main()
{
    int x;
    printf("Enter a number: ");
    scanf("%d", &x);
    if (isEven(x))
        printf("\nEven");
    else
        printf("\nOdd");
}