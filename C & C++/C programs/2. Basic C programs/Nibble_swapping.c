// Program to swap nibbles of an unsigned character
#include <stdio.h>

int main()
{
    unsigned char c = 0x8a;
    c = c << 4 | c >> 4;
    printf("%x", c);
    return 0;
}