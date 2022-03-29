// -----Loops in C-----
#include <stdio.h>

void main()
{
    // For loop
    for (int i = 0; i < 67; i++)
    {
        printf("%d ", i);
    }

    printf("\n\n");

    // While loop
    int index = 0;
    while (index < 10)
    {
        printf("%d ", index);
        index++;
    }

    printf("\n\n");

    // Do-while loop
    int j = 0;
    do
    {
        printf("do while loop is running\n");
        ++j;
    } while (j < 10);
}