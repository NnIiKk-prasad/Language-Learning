// -----Functions in C-----
#include <stdio.h>

void func1(void);     // global decleration
void func2(int, int); // global decleration
int func3(void);      // global decleration
int func4(int, int);  // global decleration

// Takes nothing and returns noting
void func1() // function definition
{
    int a, b;
    printf("\nEnter two numbers:\n");
    scanf("%d%d", &a, &b);
    printf("Sum by func1 is %d\n", a + b);
}

// Takes something and returns noting
void func2(int a, int b) // a and b are formal arguments
{
    int c;
    c = a + b;
    printf("Sum by func2 is %d\n", c);
}

// Takes nothing and returns someting
int func3()
{
    int a, b, c;
    printf("\nEnter two numbers:\n");
    scanf("%d%d", &a, &b);
    c = a + b;
    return (c);
}

// Takes something and returns someting
int func4(int a, int b)
{
    return (a + b);
}

void main()
{
    int x, y, s;

    func1(); // function call

    printf("\nEnter two numbers:\n");
    scanf("%d%d", &x, &y);
    func2(x, y); // actual arguments : call by value

    s = func3();
    printf("Sum by func3 is %d\n", s);

    printf("\nEnter two numbers:\n");
    scanf("%d%d", &x, &y);
    s = func4(x, y);
    printf("Sum by func4 is %d\n", s);
}