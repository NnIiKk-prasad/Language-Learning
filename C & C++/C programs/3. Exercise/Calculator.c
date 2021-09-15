// -----Calculator-----
#include <stdio.h>
#include <stdlib.h>

void sum(int, int);
void diff(int, int);
void mul(int, int);
void divide(int, int);

void sum(int x, int y)
{
    printf("Sum of %d and %d is %d\n", x, y, x + y);
}

void diff(int x, int y)
{
    printf("Difference of %d and %d is %d\n", x, y, x - y);
}

void mul(int x, int y)
{
    printf("Product of %d and %d is %d\n", x, y, x * y);
}

void divide(int x, int y)
{
    float t;
    t = (float)x / y;
    printf("%d divided by %d is %f\n", x, y, t);
}

int menu()
{
    int ch;
    printf("\n\n1. Sum");
    printf("\n2. Difference");
    printf("\n3. Multiply");
    printf("\n4. Divide");
    printf("\n5. Exit");
    printf("\nEnter your choice: ");
    scanf("%d", &ch);
    return ch;
}

int main()
{
    int x, y, ch;
    printf("-----Calculator-----");
    while (1)
    {
        ch = menu();
        if (ch == 1 || ch == 2 || ch == 3 || ch == 4)
        {
            printf("\nEnter two numbers:\n");
            scanf("%d%d", &x, &y);
        }
        switch (ch)
        {
        case 1:
            sum(x, y);
            break;
        case 2:
            diff(x, y);
            break;
        case 3:
            mul(x, y);
            break;
        case 4:
            divide(x, y);
            break;
        case 5:
            exit(0);
        default:
            printf("\nInvalid choice");
        }
    }
    return 0;
}
