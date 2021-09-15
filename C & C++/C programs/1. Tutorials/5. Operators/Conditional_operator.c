// -----Conditional Operator in C-----
#include <stdio.h>

void main()
{
    int c;
    c = 5 > 4 ? 1, 2, 3 : 4, 5, 6;
    printf("%d\n", c);

    int a = 4, b = 5, x;
    a > b ? x = a : (x = b);
    printf("%d\n", x);
}