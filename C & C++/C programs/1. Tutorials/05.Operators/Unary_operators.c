// -----Unary Operators in C-----
#include <stdio.h>

int main()
{
    /*Unary operators: +, -, ++, --, sizeof, etc*/

    // Increment operator
    int x = 4, y;
    ++x; // x = x + 1  Pre Increment
    printf("%d\n", x);

    x++; // x = x + 1  Post Increment
    printf("%d\n", x);

    y = x++;
    printf("%d %d\n", x, y);

    // Decrement operator
    int a = 4, b;
    --a; // a = a + 1  Pre Decrement
    printf("%d\n", a);

    a--; // a = a + 1  Post Decrement
    printf("%d\n", a);

    b = a--;
    printf("%d %d\n", a, b);

    // Sizeof operator
    printf("The size taken by int is: %d\n", sizeof(int));
    printf("The size taken by unsigned int is: %d\n", sizeof(unsigned int));
    printf("The size taken by float is: %d\n", sizeof(float));
    printf("The size taken by double is: %d\n", sizeof(double));
    printf("The size taken by long double is: %d\n", sizeof(long double));
    printf("The size taken by sort int is: %d\n", sizeof(short int));
    printf("The size taken by char: %d\n", sizeof(char));
    printf("The size taken by unsigned char is: %d\n", sizeof(unsigned char));
}