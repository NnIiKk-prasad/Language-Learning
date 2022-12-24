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
    ptr = malloc(sizeof(float));
    if (ptr == NULL)
    {
        printf("Error allocating memory\n");
        exit(EXIT_FAILURE);
    }
    *ptr = 4.5;
    printf("Value stored in dynamically allocated memory: %f\n", *ptr);
    
    // calloc()
    int *p;
    p = calloc(3, sizeof(int));
    *(p + 0) = 34;
    *(p + 1) = 78;
    printf("Values stored in dynamically allocated memory using calloc: %d, %d\n", *(p + 0), *(p + 1));

    // realloc()
    int *q;
    q = realloc(p, 5 * sizeof(int));
    if (q == NULL)
    {
        printf("Error reallocating memory\n");
        exit(EXIT_FAILURE);
    }
    printf("Values stored in dynamically allocated memory using realloc: %d, %d\n", *(p + 1), *(q + 1));

    // free()
    free(ptr);
    free(p);
    free(q);
}