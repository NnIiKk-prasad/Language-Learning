// -----Nested If - Else-----
#include <stdio.h>
void main()
{
    // Program to find greatest of three numbers
    int x, a, b, c;
    printf("Enter three numbers:\n");
    scanf("%d%d%d", &a, &b, &c);

    // if (a > b)
    // {
    //     if (a > c)
    //         printf("%d", a);
    //     else
    //         printf("%d", b);
    // }
    // else
    // {
    //     if (b > c)
    //         printf("%d", b);
    //     else
    //         printf("%d", c);
    // }

    x = a > b ? (a > c ? a : c) : (b > c ? b : c);
    printf("Greatest no. is %d", x);
}
