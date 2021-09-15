// -----Dynamic Memory Allocation in C-----
#include <stdio.h>
#include <stdlib.h>

void fun(void);

void main()
{
    fun();
}

void fun()
{
    // malloc()
    float *ptr;
    ptr = malloc(4);
    *ptr = 4.5;

    // calloc()
    int *p;
    p = calloc(5, 2);
    *(p + 0) = 34;
    *(p + 1) = 78;

    // realloc()
    int *q;
    q = realloc(ptr, 8);

    // free()
    free(ptr);
    free(p);
    free(q);
}