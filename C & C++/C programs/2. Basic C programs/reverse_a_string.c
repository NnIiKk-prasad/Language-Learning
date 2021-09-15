// Iterative C program to reverse an array
#include <stdio.h>

int length(char *p)
{
    int i = 0;
    while (p[i] != '\0')
        i++;
    return (i);
}

void reverse(char *p)
{
    int start = 0, end;
    // char temp;
    end = length(p) - 1;
    while (start < end)
    {
        // temp = p[start];
        // p[start] = p[end];
        // p[end] = temp;

        // XOR for swapping the variable
        p[start] ^= p[end];
        p[end] ^= p[start];
        p[start] ^= p[end];
        ++start;
        --end;
    }
}

void main()
{
    char str[20];
    printf("Enter a string: ");
    gets(str);
    printf("\nLength of string is %d\n", length(str));
    reverse(str);
    printf("\nReversed string is %s\n", str);
}
