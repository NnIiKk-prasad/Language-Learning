// -----Pointers in C-----
#include <stdio.h>

void main()
{
    int x = 100, *j;
    j = &x;
    printf("%d %u", x, j);
    printf("\n%d %u", *j, &x);
    printf("\n%u", *&j);
}
