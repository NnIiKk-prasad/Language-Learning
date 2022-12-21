// -----Some special pointers----
#include <stdio.h>

void fun1(void);
int fun2(int);

void main()
{
    int *r = NULL;  // Null pointer
    
    fun1();

    // Function pointer
    int (*p)(int); // decleration of function pointer
    p = fun2;
    printf("%d\n", p(5));

    // Generic or void pointer
    int x = 6;
    float y = 3.14;
    void *q;

    q = &x;
    *(int*)q = 8;

    q = &y;
    *(float*)q = 6.9;

    printf("x = %d y = %f", x, y);
}

void fun1()
{
    int *p;  // uninitialized or wild pointer
    {
        int x;
        p = &x;
    }
    // After the above block ends, 'p' will become a dangling pointer, as the address stored in 'p' becomes invalid.
}

int fun2(int x)
{
    return (x + 1);
}