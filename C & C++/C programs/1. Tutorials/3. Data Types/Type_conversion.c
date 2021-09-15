// -----Type Conversion-----
#include <stdio.h>

int main()
{
    // Implicit Type Conversion
    int x = 10;   // integer x
    char y = 'a'; // character c

    x = x + y;         // y implicitly converted to int. ASCII value of 'a' is 97
    float z = x + 1.0; // x is implicitly converted to float

    printf("\nx = %d, z = %f", x, z);

    // Explicit Type Conversion
    double a = 1.2;

    int sum = (int)a + 1; // Explicit conversion from double to int

    printf("\nsum = %d", sum);
    return 0;
}