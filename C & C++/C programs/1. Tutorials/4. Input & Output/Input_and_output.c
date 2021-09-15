// -----Input & Output instructions in C-----
#include <stdio.h>

void main()
{
    printf("Nikhil Prasad\n");

    int a = 6, b = 5;
    /*format specifiers:
        %d - int
        %f - float
        %lf - double
        %c - char
        %s - string
    */
    printf("a = %d and b = %d", a, b);

    int x;
    printf("\n\nEnter the value of x: ");
    scanf("%d", &x);
    printf("x = %d", x);
}