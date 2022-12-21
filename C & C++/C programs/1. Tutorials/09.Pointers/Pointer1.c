// -----Pointers in C-----
#include <stdio.h>

void main()
{
    int x = 100, *j;
    j = &x;
    printf("%d %u", x, j);
    printf("\n%d %u", *j, &x);
    printf("\n%u", *&j);

    // It is generally not a good idea to use the %u format specifier to print the value of a pointer, because pointers are typically stored as signed integers and the %u format specifier is used to print unsigned integers. Instead, it is better to use the %p format specifier to print the value of a pointer.
    printf("\n\n%d %p", x, (void*)j);
    printf("\n%d %p", *j, (void*)&x);
    printf("\n%p", (void*)*&j);
}
