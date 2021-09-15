// Swapping of numbers using pointers
#include <stdio.h>
#include <stdlib.h>

void swap(int *a, int *b)
{
    int t;
    t = *a;
    *a = *b;
    *b = t;
}

int main()
{
    int a, b;
    printf("Enter two numbers:\n");
    scanf("%d%d", &a, &b);
    swap(&a, &b);
    printf("a=%d and b=%d", a, b);
    getchar();
    return 0;
}
