// -----Union in C-----
#include <stdio.h>

union item
{
    int x;
    float y;
    char z;
};

union a
{
    int i;
    // short int i; // To enforce little-endian output.
    char ch[2];
};

int main()
{
    union item i1;
    i1.x = 5;
    printf("%d ", i1.x);

    i1.y = 34.5;
    printf("%f ", i1.y);
    
    i1.z = 'a';
    printf("%c\n", i1.z);

    union a u;
    u.ch[0] = 3;
    u.ch[1] = 2;
    printf("%d, %d, %d\n", u.ch[0], u.ch[1], u.i);
    return 0;
}
